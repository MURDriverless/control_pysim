from ..world.car import Car


class State:
    """
    Container class to store the estimated vehicle state

    Notes:
        We use a class to contain the state instead of list, as the positional index
        of a list can sometimes be confusing to interpret, depending on the choice of states.
        The keyword indexes in this class aim to remove that confusion.
    """
    def __init__(self, x, y, linear_velocity, yaw):
        self.x = x
        self.y = y
        self.linear_velocity = linear_velocity
        self.yaw = yaw

    @classmethod
    def from_array(cls, array):
        """ Format: [x, y, linear_velocity, yaw, angular_velocity] """
        return cls(array[0], array[1], array[2], array[3])

    @classmethod
    def from_car(cls, car):
        """
        Args:
            car (Car): a Car object as specified in src.world.car
        """
        return cls(car.x, car.y, car.linear_velocity, car.yaw)
