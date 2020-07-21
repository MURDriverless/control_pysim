class State:
    """
    Container class to store the data from Perception team at a given time

    Notes:
        We use a class to contain the state instead of list, as the positional index
        of a list can sometimes be confusing to interpret depending on the choice of states.
        The keyword indexes in this class aim to remove that confusion.
    """
    x = 0.0
    y = 0.0
    linear_velocity = 0.0
    yaw = 0.0
    angular_velocity = 0.0
    steering_angle = 0.0
    left_cones = []
    right_cones = []

    @classmethod
    def update_from_array(cls, array):
        cls.x = array[0]
        cls.y = array[1]
        cls.linear_velocity = array[2]
        cls.yaw = array[3]
        cls.angular_velocity = array[4]
        cls.steering_angle = array[5]
        cls.left_cones = array[6]
        cls.right_cones = array[7]
