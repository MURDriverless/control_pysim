from abc import ABC, abstractmethod
from ..perception.slam_data import SLAMData
from .planner_data import PlannerData


class PathPlanningInterface(ABC):
    @abstractmethod
    def plan(self, slam_data):
        """
        Generate optimal path to traverse along the racing track

        Args:
            slam_data (SLAMData): output from the Perception team via SLAM

        Returns:
            PlannerData
        """
        pass
