import os
from stable_baselines3 import PPO
from rl_fuzz_env import AFLFuzzEnv

# Load the trained RL model
model = PPO.load("/home/kios/AFLplusplus/adaptive_fuzzer")

# Initialize fuzzing environment
env = AFLFuzzEnv()

# ✅ Extract only the observation from reset()
obs, _ = env.reset()

for step in range(1000):  # Run for 1000 steps
    action, _ = model.predict(obs)

    # ✅ Define mutation strategies
    mutation_types = ["bitflip", "havoc", "splice", "trim"]
    selected_mutation = mutation_types[action]
    
    # ✅ Debug Output
    print(f"[DEBUG] Step {step}: AI selected mutation - {selected_mutation}")

    # ✅ Use absolute paths for AFL++ execution
    afl_command = (
        f"afl-fuzz -i /home/kios/AFLplusplus/inputs "
        f"-o /home/kios/AFLplusplus/outputs "
        f"-M adaptive_fuzzer -- "
        f"/home/kios/AFLplusplus/target_binary "
        f"-m {selected_mutation}"
    )
    
    print(f"[DEBUG] Running: {afl_command}")  # Debug output
    
import subprocess
import csv

# Run AFL++ with proper error handling
try:
    result = subprocess.run(afl_command, shell=True, check=True, timeout=600)
    success = True
except subprocess.TimeoutExpired:
    print("[ERROR] AFL++ Timeout Reached")
    success = False
except subprocess.CalledProcessError as e:
    print(f"[ERROR] AFL++ Execution Failed: {e}")
    success = False

# Log AFL++ execution results in CSV format
log_file_path = "/home/kios/AFLplusplus/mutation_log.csv"
with open(log_file_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([step, selected_mutation, reward, success])
      # Execute AFL++ directly

    # ✅ Step in the environment
    obs, reward, done, truncated, _ = env.step(action)

    # ✅ Log AI-guided mutation to file
    with open("/home/kios/AFLplusplus/mutation_log.txt", "a") as log_file:
        log_file.write(f"Step {step}: Mutation - {selected_mutation}, Reward - {reward}\n")

    # ✅ Stop if fuzzing session completes
    if done or truncated:
        obs, _ = env.reset()

