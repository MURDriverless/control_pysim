from abc import ABC, abstractmethod
from ..perception.state import State
from ..path_planning.optimal_path import OptimalPath
from .actuation_data import ActuationData


class PathTrackingInterface(ABC):
    @abstractmethod
    def control(self, state, optimal_path):
        """
        Generate actuation commands to track the planned optimal path

        Args:
            state (State): state of the car at a given time
            optimal_path (OptimalPath): container to store optimal way-points as a list

        Returns:
            ActuationData
        """
        pass
