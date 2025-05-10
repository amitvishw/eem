from src.Robot import Robot

class Mission:
    def __init__(self, plateau):
        self.plateau = plateau
        self.robots = []

    def deploy_robot(self, initial_x_position, initial_y_position, initial_direction, instructions):
        robot = Robot(self.plateau, initial_x_position, initial_y_position, initial_direction, instructions)
        self.robots.append(robot)

    def execute(self):
        results = []
        for robot in self.robots:
            robot.execute_instructions()
            results.append(robot.get_position())
        return results
