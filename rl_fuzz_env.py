import gym
import numpy as np
import subprocess
from gym import spaces

class AFLFuzzEnv(gym.Env):
    def __init__(self):
        super(AFLFuzzEnv, self).__init__()

        # Observation space: AFL++ stats (coverage, crashes, execution speed)
        self.observation_space = spaces.Box(low=0, high=100, shape=(3,), dtype=np.float32)

        # Action space: Mutation strategies (bit flips, havoc, splicing, trimming)
        self.action_space = spaces.Discrete(4)

        self.previous_coverage = 0

    def step(self, action):
        # Define mutation types
        mutation_types = ["bitflip", "havoc", "splice", "trim"]
        selected_mutation = mutation_types[action]

        # Run AFL++ with the selected mutation strategy
        afl_command = f"afl-fuzz -i inputs -o outputs -M adaptive_fuzzer -- ./target_binary -m {selected_mutation}"
        subprocess.run(afl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Extract AFL++ statistics (Simulated values for now)
        coverage, crashes, exec_speed = self.get_afl_stats()

        # Reward function: Encourage better coverage, discourage crashes
        reward = (coverage - self.previous_coverage) * 10 - crashes * 5
        self.previous_coverage = coverage

        done = False  # Continuous training
        truncated = False  # New API requires this (Stable-Baselines3 v2.0+)

        return np.array([coverage, crashes, exec_speed], dtype=np.float32), reward, done, truncated, {}

    def reset(self, seed=None, options=None):
        # Reset AFL++ fuzzing state before training
        subprocess.run("rm -rf outputs/*", shell=True)
        subprocess.run("mkdir -p outputs", shell=True)
        self.previous_coverage = 0

        return np.array([0, 0, 0], dtype=np.float32), {}

    def get_afl_stats(self):
        # Extract AFL++ stats (Simulated values for testing)
        coverage = np.random.randint(10, 50)  
        crashes = np.random.randint(0, 1)  
        exec_speed = np.random.randint(2000, 5000)  

        return coverage, crashes, exec_speed
