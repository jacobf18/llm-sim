# TODO: Write a dynamic environment for the mountain car domain.
# The gravity of the environment will change drastically after 100 steps.
# We can set this level of drastic change, but the changes will not be continuous.
# We can include 3 levels of changes: low, medium, and high.

from gymnasium.envs.classic_control.mountain_car import MountainCarEnv

class DynamicMountainCarEnv(MountainCarEnv):
    def __init__(self, gravity=0.0025, low_gravity=0.0005, medium_gravity=0.0025, high_gravity=0.25, **kwargs):
        super(DynamicMountainCarEnv, self).__init__(**kwargs)
        self.gravity = low_gravity
        self.low_gravity = low_gravity
        self.medium_gravity = medium_gravity
        self.high_gravity = high_gravity
        self.steps = 0

    def step(self, action, **kwargs):
        """Move one time step forward. Change the gravity of the environment
        at specific time steps.

        Args:
            action (int): Action to take.
        """
        self.steps += 1
        if self.steps == 250:
            print('Low gravity')
            self.gravity = self.low_gravity
        elif self.steps == 500:
            print('Medium gravity')
            self.gravity = self.medium_gravity
        elif self.steps == 750:
            print('High gravity')
            self.gravity = self.high_gravity
        return super(DynamicMountainCarEnv, self).step(action, **kwargs)

    def reset(self, **kwargs):
        self.steps = 0
        return super(DynamicMountainCarEnv, self).reset(**kwargs)