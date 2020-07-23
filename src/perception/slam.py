from .slam_data import SLAMData
from .state import State
from .cone_finder import find_nearest_cone


class SLAM:
    def __init__(self, searchable_size):
        self.left_index = 0
        self.right_index = 0
        self.searchable_size = searchable_size

    def update(self, car, all_left_cones, all_right_cones):
        # Obtain vehicle state
        state = State.from_car(car)

        # Get the first nearest left and right cone in terms of index
        self.left_index = find_nearest_cone(car.x, car.y, all_left_cones, self.left_index, self.searchable_size)
        self.right_index = find_nearest_cone(car.x, car.y, all_right_cones, self.right_index, self.searchable_size)

        # Obtain a list of N nearest left and right cones in front of the car, and update the state
        left_cones = all_left_cones[self.left_index:(self.left_index + self.searchable_size + 1)]
        right_cones = all_right_cones[self.right_index:(self.right_index + self.searchable_size + 1)]

        # For the cones detected by SLAM, toggle them so they will be rendered
        [cone.set_detected(True) for cone in left_cones + right_cones]

        # Return the updated state
        return SLAMData(state, left_cones, right_cones)
