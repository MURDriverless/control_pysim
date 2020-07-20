import math
import matplotlib.pyplot as plt
from src.models.track import Track
from src.models.car import Car


# Test plotting with animation
def animated_plot():
    # Generate points
    xs = [i for i in range(-5, 6)]
    ys = [x**2 for x in xs]
    dt = 0.2

    # Start plotting
    plt.cla()
    # For stopping simulation with the esc key.
    plt.gcf().canvas.mpl_connect('key_release_event', lambda event: [exit(0) if event.key == 'escape' else None])

    # Plot data points
    for i in range(len(xs)):
        plt.plot(xs[i], ys[i], "bx-")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        # Prevent axes from expanding by setting limits. They must be defined here,
        # if it is applied outside, only the last point gets applied.
        plt.xlim(-5, 5)
        plt.ylim(0, 25)
        plt.pause(dt)

    # Finally render the plot
    plt.show()


def test_plot_track():
    # Initialise objects
    track_name = "fsg_alex.txt"
    track = Track(track_name)
    init_x = (track.left_cones[0].x + track.right_cones[0].x) / 2.0
    init_y = (track.left_cones[0].y + track.right_cones[0].y) / 2.0
    car = Car(init_x, init_y, 0.0)

    # Plot initial positions
    track.plot()
    car.plot()

    # Plot subsequent simulation positions
    for i in range(10):
        car.move(5, (math.pi / 180.0)*-30)  # 5m/s^2 & 30 degree steering to the right
        plt.cla()
        track.plot()
        car.plot()
        plt.pause(0.2)

    # Render
    plt.show()


if __name__ == "__main__":
    test_plot_track()
