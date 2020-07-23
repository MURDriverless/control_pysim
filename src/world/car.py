import math
import matplotlib.pyplot as plt


class Car:
    def __init__(self, init_x, init_y, init_yaw):
        self.x = init_x
        self.y = init_y
        self.linear_velocity = 0.0
        self.yaw = init_yaw
        self.angular_velocity = 0.0
        self.steering_angle = 0.0    # steering angle

    def plot(self):
        plt.plot(self.x, self.y, "kx")

    def move(self, acceleration, steering):
        # TODO: Update vehicle model from kinematic to dynamic bicycle model
        dt = 0.2
        L = 2.5  # length of vehicle from front to back
        
        # Kinematic bicycle model
        self.x = self.x + dt * (self.linear_velocity * math.cos(self.yaw))
        self.y = self.y + dt * (self.linear_velocity * math.sin(self.yaw))
        self.linear_velocity = self.linear_velocity + dt * acceleration
        self.yaw = self.yaw + dt * (self.linear_velocity * math.tan(self.steering_angle) / L)
        # self.angular_velocity is assumed to not affect the car dynamics
        self.steering_angle = self.steering_angle + dt * steering
