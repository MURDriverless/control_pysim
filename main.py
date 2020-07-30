import matplotlib.pyplot as plt
from src.world.environment import Environment
from src.path_planning.centre_track import CentreTrack
from src.path_tracking.pid_pure_pursuit import PIDPurePursuit


def simulation():
    """
    Steps:
    1. Create track (cones + time keeper)
    2. Create car
    3. Create first loop, which is the slow lap. Record total time taken and store the state of the vehicle over time.
    4. In the slow lap, for each time step (increasing dt from start to end of lap):
        a. Obtain environment data via SLAM, and check if car has finished one lap.
        b. Call Path Planner to produce space-domain reference.
        c. Call Path Follower to generate time-domain reference and track the optimal path.
    5. In the fast lap:
        a. Generate space-domain reference at the start of each lap using Path Planner.
        b. At every time step, obtain environment data via SLAM, and check if the car has finished one lap.
        c. At every time step, call Path Follower to track the optimal path using current vehicle state
           and the optimal path generated at the start of the lap.
    """
    # Simulation parameters
    fps = 5
    dt = 1/fps
    max_time = 100
    t = 0.0

    # Set up simulation
    env = Environment("fsg_alex.txt", 4, dt)  # SLAM can only discover up to 4 cones on each side
    env.plot()
    # Get initial observations
    slam_data = env.slam.update(env.car, env.left_cones, env.right_cones)
    planned_path = None

    # Create Path Planner and Follower
    planner = CentreTrack(10, 0.5)  # Generate reference from 0 to 10m (approx. 2 cones ahead) with step size of 0.5m
    follower = PIDPurePursuit()

    # Run simulation
    while t < max_time:
        # Plot the result
        env.plot()
        # Plan path based on initial observations
        planned_path = planner.plan(slam_data)
        # From planned path, generate actuation command
        actuation = follower.control(slam_data, planned_path)
        # Get observations from SLAM after applying the actuation
        slam_data = env.update(actuation)
        # Increment timer
        t += dt
        # Introduce pause for animation purposes
        plt.pause(dt)

    plt.show()


if __name__ == "__main__":
    simulation()
