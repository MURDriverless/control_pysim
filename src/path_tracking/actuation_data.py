class ActuationData:
    """
    Container class to hold data for actuation commands

    Attributes:
        - acceleration (float): threshold ranging from -1.0 (max. braking) and 1.0 (max. acceleration)
        - steering (float): threshold ranging from -1.0 (leftmost turn) and 1.0 (rightmost turn)
    """
    acceleration = 0.0
    steering = 0.0

    def __init__(self, acceleration, steering):
        # Limit actuation to upper and lower bounds
        if acceleration > 1.0:
            acceleration = 1.0
        elif acceleration < -1.0:
            acceleration = -1.0
        if steering > 1.0:
            steering = 1.0
        elif steering < -1.0:
            steering = -1.0

        self.acceleration = acceleration
        self.steering = steering
