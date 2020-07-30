import numpy as np
from ..utils.cubic_spline import Spline2D
from .interface import PathPlanningInterface
from .planner_data import PlannerData


class CentreTrack(PathPlanningInterface):
    def __init__(self, max_distance, step_size):
        self.max_distance = max_distance
        self.step_size = step_size

    def plan(self, slam_data):
        left_cones = slam_data.left_cones
        right_cones = slam_data.right_cones

        middle_x = [(left.x + right.x) / 2.0 for left, right in zip(left_cones, right_cones)]
        middle_y = [(left.y + right.y) / 2.0 for left, right in zip(left_cones, right_cones)]
        spline = Spline2D(middle_x, middle_y)

        interval = np.arange(0, self.max_distance, self.step_size)
        points = [spline.interpolate(i) for i in interval]
        return PlannerData(points)
