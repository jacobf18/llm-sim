import gymnasium as gym

description = """
The Mountain Car MDP is a deterministic MDP that consists of a car placed stochastically at the bottom of a sinusoidal valley, with the only possible actions being the accelerations that can be applied to the car in either direction. The goal of the MDP is to strategically accelerate the car to reach the goal state on top of the right hill. There are two versions of the mountain car domain in gymnasium: one with discrete actions and one with continuous. This version is the one with continuous actions.
"""

# The dynamics of the system are defined by the following equations:
# velocity_{t+1} = velocity_t + (action - 1) * force - cos(3 * position_t) * gravity
# position_{t+1} = position_t + velocity_{t+1}

env = gym.make("MountainCar-v0", render_mode="human")
observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    episode_over = terminated or truncated

env.close()