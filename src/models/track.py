from pathlib import Path
import csv
from src.utils.project_root import PROJECT_ROOT
from src.models.cone import Cone


class Track:
    def __init__(self, file_name):
        self.left_cones, self.right_cones = self.load_track(file_name)

    def plot(self):
        [cone.plot() for cone in self.left_cones + self.right_cones]

    @staticmethod
    def load_track(file_name):
        left_cones, right_cones = [], []
        try:
            # Build path
            file_path = Path(PROJECT_ROOT).joinpath("./tracks", file_name)
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
            print(f"File {file_name} not found")
