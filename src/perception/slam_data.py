from .state import State
from ..world.cone import Cone


class SLAMData:
    """
    Container class to store the data from Perception team at a given time

    Attributes:
        state (State): estimated vehicle state
        left_cones (list of Cone): currently perceived left cones in front of the car
        right_cones (list of Cone): currently perceived right cones in front of the car

    """
    def __init__(self, state, left_cones, right_cones):
        self.state = state
        self.left_cones = left_cones
        self.right_cones = right_cones
