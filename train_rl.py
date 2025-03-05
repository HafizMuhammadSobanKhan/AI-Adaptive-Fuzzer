from stable_baselines3 import PPO
from rl_fuzz_env import AFLFuzzEnv

# Initialize the fuzzing environment
env = AFLFuzzEnv()

# Train the RL agent using Proximal Policy Optimization (PPO)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=500)  # Train for 10,000 steps

# Save the trained model
model.save("adaptive_fuzzer")
model.save("/home/kios/AFLplusplus/adaptive_fuzzer")
print("Training complete! Model saved as adaptive_fuzzer.")
