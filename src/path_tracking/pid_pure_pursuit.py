import math
import matplotlib.pyplot as plt
from .interface import PathTrackingInterface
from .actuation_data import ActuationData


class PIDPurePursuit(PathTrackingInterface):
    def __init__(self):
        # PID parameters
        self.target_speed = 20.0 * (1 / 3.6)  # 20.0 km/h
        self.Kp = 1  # Linear velocity P gain

        # Pure Pursuit parameters
        self.WB = 2.9  # Length from front to back of the wheel base
        self.k = 0.1  # Look-forward gain (multiplied by linear velocity)
        self.Lfc = 2  # Look-ahead distance constant

    def control(self, slam_data, planner_data):
        x = slam_data.state.x
        y = slam_data.state.y
        linear_velocity = slam_data.state.linear_velocity
        yaw = slam_data.state.yaw

        # Control law for forward acceleration
        acceleration = self.acceleration_control(self.target_speed, linear_velocity)

        # Find target x,y
        target_index, Lf = self.search_target_index(slam_data.state, planner_data.points)

        # Plot the look-ahead point for visual purposes
        target_x = planner_data.points[target_index][0]
        target_y = planner_data.points[target_index][1]
        plt.plot(target_x, target_y, "ro")

        # Control law for steering
        steering = self.steering_control(x, y, yaw, target_x, target_y, Lf)

        return ActuationData(acceleration, steering)

    def acceleration_control(self, target_speed, current_speed):
        return self.Kp * (target_speed - current_speed)

    def steering_control(self, x, y, yaw, target_x, target_y, Lf):
        rear_x, rear_y = self.calculate_rear_position(x, y, yaw)
        alpha = math.atan2(target_y - rear_y, target_x - rear_x) - yaw
        return math.atan2(2.0 * self.WB * math.sin(alpha) / Lf, 1.0)

    def search_target_index(self, state, waypoints):
        # Unpack state
        x = state.x
        y = state.y
        linear_velocity = state.linear_velocity
        yaw = state.yaw

        # Get look-ahead distance
        Lf = self.k * linear_velocity + self.Lfc

        # Calculate the distance from current car position to the first point in
        # planned path
        index = 0
        point_x = waypoints[index][0]
        point_y = waypoints[index][1]
        index_distance = self.calculate_rear_to_target(x, y, yaw, point_x, point_y)

        # Iterate through each point in the planned path until we get the furthest point
        # according to Lf, or if we are at the end-point.
        while index_distance < Lf:
            if (index + 1) >= len(waypoints):
                break
            # Since we are still in iteration, increment the index
            index += 1
            # Recalculate the distance to check if we have reached the furthest point
            point_x = waypoints[index][0]
            point_y = waypoints[index][1]
            index_distance = self.calculate_rear_to_target(x, y, yaw, point_x, point_y)
        return index, Lf

    def calculate_rear_position(self, x, y, yaw):
        rear_x = x - ((self.WB / 2.0) * math.cos(yaw))
        rear_y = y - ((self.WB / 2.0) * math.sin(yaw))
        return rear_x, rear_y

    def calculate_rear_to_target(self, x, y, yaw, target_x, target_y):
        rear_x, rear_y = self.calculate_rear_position(x, y, yaw)
        dx = rear_x - target_x
        dy = rear_y - target_y
        return math.hypot(dx, dy)
