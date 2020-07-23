from pathlib import Path
import csv
import matplotlib.pyplot as plt
from src.utils.project_root import PROJECT_ROOT
from src.world.car import Car
from src.world.cone import Cone
from src.path_tracking.actuation_data import ActuationData
from src.perception.slam import SLAM


class Environment:
    def __init__(self, track_name, cone_searchable_size):
        # Build track
        self.left_cones, self.right_cones = self.load_track(track_name)

        # Initialise car
        init_yaw = 0.0
        init_x, init_y = self.get_car_init_position(self.left_cones, self.right_cones)
        self.car = Car(init_x, init_y, init_yaw)

        # Initialise SLAM reporter
        self.slam = SLAM(cone_searchable_size)

        # Create list to hold x and y positions for plotting purpose
        self.xs = []
        self.ys = []

    def update(self, actuation):
        """
        Gets called every update frequency

        Args:
            actuation (ActuationData)

        Returns:
            SLAMData
        """
        # Apply actuation
        self.car.move(actuation.acceleration, actuation.steering)
        # Get slam observation
        slam_data = self.slam.update(self.car, self.left_cones, self.right_cones)

        # Append position to memory for plotting purposes
        self.xs.append(slam_data.state.x)
        self.ys.append(slam_data.state.y)

        # Finally, return slam observation
        return slam_data

    def reset(self):
        # Reset car position and yaw
        init_x, init_y = self.get_car_init_position(self.left_cones, self.right_cones)
        self.car.x = init_x
        self.car.y = init_y
        self.car.yaw = 0.0

        # Reset SLAM left and right cone index
        self.slam.left_index = 0
        self.slam.right_index = 0

        # Assign empty list to xs and ys
        self.xs = []
        self.ys = []

    def plot(self):
        # Clear axes as we are drawing from scratch
        plt.cla()
        # Plot the static cones
        [cone.plot() for cone in self.left_cones + self.right_cones]
        # Plot the trajectory of the car from start as a line
        plt.plot(self.xs, self.ys, 'k-')
        # And finally, plot the car's current position with an "x"
        self.car.plot()

    @staticmethod
    def load_track(file_name):
        left_cones, right_cones = [], []
        # Build path
        file_path = Path(PROJECT_ROOT).joinpath("./src/tracks", file_name)
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                # Discard first line as it is the description
                next(csv_reader)
                # Append subsequent lines to data
                for row in csv_reader:
                    left_cones.append(Cone(float(row[0]), float(row[1]), "bx"))
                    right_cones.append(Cone(float(row[2]), float(row[3]), "yx"))
            return left_cones, right_cones
        except FileNotFoundError:
            print(f"File {file_path} not found")

    @staticmethod
    def get_car_init_position(all_left_cones, all_right_cones):
        assert len(all_left_cones) > 0
        assert len(all_right_cones) > 0
        init_x = (all_left_cones[0].x + all_right_cones[0].x) / 2.0
        init_y = (all_left_cones[0].y + all_right_cones[0].y) / 2.0
        return init_x, init_y
