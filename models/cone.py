import matplotlib.pyplot as plt


class Cone:
    def __init__(self, x, y, plt_opts):
        self.x = x
        self.y = y
        self.detected = True
        self.plt_opts = plt_opts

    def set_detected(self, detected):
        self.detected = detected

    def plot(self):
        plt.plot(self.x, self.y, self.plt_opts) if self.detected is True else None
