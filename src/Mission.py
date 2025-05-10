from src.Robot import Robot

class Mission:
    def __init__(self, plateau):
        print(f"Mission initialized on plateau with max_x={plateau.max_x}, max_y={plateau.max_y}")
        self.plateau = plateau
        self.robots = []

    def deploy_robot(self, initial_x_position, initial_y_position, initial_direction, instructions):
        print(
            f"Deploying robot at x={initial_x_position}, y={initial_y_position}, facing={initial_direction} with instructions: {instructions}")
        robot = Robot(self.plateau, initial_x_position, initial_y_position, initial_direction, instructions)
        self.robots.append(robot)
        print(f"Robot {robot.id} successfully deployed.")

    def execute(self):
        print(f"Starting mission execution for {len(self.robots)} robot(s)...")
        results = []
        for idx, robot in enumerate(self.robots, start=1):
            print(f"Executing instructions for Robot {robot.id} (#{idx})...")
            robot.execute_instructions()
            final_position = robot.get_position()
            print(f"Robot {robot.id} final position: {final_position}")
            results.append(final_position)
        print(f"Mission execution complete.")
        return results
