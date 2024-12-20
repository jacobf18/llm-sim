import gymnasium as gym
from dynamic_gymnasium.mountain_car import DynamicMountainCarEnv

description = """
The Mountain Car MDP is a deterministic MDP that consists of a car placed stochastically at the bottom of a sinusoidal valley, with the only possible actions being the accelerations that can be applied to the car in either direction. The goal of the MDP is to strategically accelerate the car to reach the goal state on top of the right hill. There are two versions of the mountain car domain in gymnasium: one with discrete actions and one with continuous. This version is the one with continuous actions.
"""

# Register the dynamic environment
gym.register(
    id="dynamic/DynamicMountainCar-v0",
    entry_point=DynamicMountainCarEnv,
    max_episode_steps=1000
)

# The dynamics of the system are defined by the following equations:
# velocity_{t+1} = velocity_t + (action - 1) * force - cos(3 * position_t) * gravity
# position_{t+1} = position_t + velocity_{t+1}

# Gravity changes for the dynamic mountain car environment drastically at 2 points.
# It starts out at 0.0005 (time 0-499), then 0.0025 (time 500-749), then 0.25 (time 750-999).

env = gym.make("dynamic/DynamicMountainCar-v0", render_mode="human")

observation, info = env.reset()

# We can access the gravity parameter of the environment through
# the unwrapped attribute of the environment
# print(env.unwrapped.gravity)
# The default value is 0.0025

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    episode_over = terminated or truncated

env.close()