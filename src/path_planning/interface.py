from abc import ABC, abstractmethod
from ..perception.state import State
from .optimal_path import OptimalPath


class PathPlanningInterface(ABC):
    @abstractmethod
    def plan(self, state):
        """
        Generate optimal path to traverse along the racing track

        Args:
            state (State): state of the car at a given time

        Returns:
            OptimalPath
        """
        pass
