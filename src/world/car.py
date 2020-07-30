import math
import matplotlib.pyplot as plt


class Car:
    def __init__(self, init_x, init_y, init_yaw, dt):
        # Discretisation parameters
        self.dt = dt

        # Model-specific parameters
        self.WB = 2.9  # Length from front to back of wheel base

        # State
        self.x = init_x
        self.y = init_y
        self.linear_velocity = 0.0
        self.yaw = init_yaw
        self.WB = 2.9
        self.dt = dt

        # States over time
        self.xs = []
        self.ys = []
        self.linear_velocities = []
        self.yaws = []

    def move(self, acceleration, steering):
        # TODO: Update vehicle model from kinematic to dynamic bicycle model

        # Update state
        self.x += self.linear_velocity * math.cos(self.yaw) * self.dt
        self.y += self.linear_velocity * math.sin(self.yaw) * self.dt
        self.linear_velocity += acceleration * self.dt
        self.yaw += self.linear_velocity / self.WB * math.tan(steering) * self.dt

        # Append the state to collection
        self.xs.append(self.x)
        self.ys.append(self.y)
        self.linear_velocities.append(self.linear_velocity)
        self.yaws.append(self.yaw)

    def plot(self, plt_colour="k"):
        # Plot past locations
        plt.plot(self.xs, self.ys, plt_colour + "-")
        # Plot current location
        plt.plot(self.x, self.y, plt_colour + "x")
