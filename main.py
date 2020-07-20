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


def simulation():
    """
    Steps:
    1. Create track (cones + time keeper)
    2. Create car
    3. Create first loop, which is the slow lap. Record total time taken and store the state of the vehicle over time.
    4. In the slow lap, for each time step (increasing dt from start to end of lap):
        a. Obtain environment data via SLAM
        b. Call Path Planner to produce space-domain reference
        c. Call Path Follower to generate time-domain reference and track the optimal path
    5. In the fast lap:
        a. Generate space-domain reference at the start of each lap using Path Planner.
        b. At every time step, obtain environment data via SLAM
        c. At every time step, call Path Follower to track the optimal path using current vehicle state
           and the optimal path generated at the start of the lap.
    """
    pass


if __name__ == "__main__":
    test_plot_track()
