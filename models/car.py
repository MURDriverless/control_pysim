import math
import matplotlib.pyplot as plt


class Car:
    def __init__(self, init_x, init_y, init_yaw):
        self.x = init_x
        self.y = init_y
        self.v = 0.0
        self.yaw = init_yaw
        self.delta = 0.0    # steering angle

    def plot(self):
        plt.plot(self.x, self.y, "kx")

    def move(self, acceleration, steering):
        # TODO: Update vehicle model from kinematic to dynamic bicycle model
        dt = 0.2
        L = 2.5  # length of vehicle from front to back
        # Kinematic bicycle model
        self.x = self.x + dt * (self.v*math.cos(self.yaw))
        self.y = self.y + dt * (self.v*math.sin(self.yaw))
        self.v = self.v + dt * acceleration
        self.yaw = self.yaw + dt * (self.v*math.tan(self.delta)/L)
        self.delta = self.delta + dt * steering
