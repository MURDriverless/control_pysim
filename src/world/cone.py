import matplotlib.pyplot as plt


class Cone:
    def __init__(self, x, y, plt_opts):
        self.x = x
        self.y = y
        self.detected = False
        self.plt_opts = plt_opts

    def set_detected(self, detected):
        self.detected = detected

    def plot(self):
        # If the cone is not detected yet, still render it as a white "x" so the axes don't scale out of order
        plt.plot(self.x, self.y, self.plt_opts) if self.detected is True else plt.plot(self.x, self.y, "wx")
