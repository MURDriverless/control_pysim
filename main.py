import matplotlib.pyplot as plt
from models.track import Track


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
    track_name = "fsg_alex.txt"
    track = Track(track_name)
    track.plot()
    plt.show()


if __name__ == "__main__":
    test_plot_track()
