from src.Mission import Mission
from src.Plateau import Plateau

if __name__ == "__main__":
    input_str = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""
    lines = input_str.strip().split('\n')
    max_x, max_y = map(int, lines[0].split())
    robot_data = lines[1:]
    plateau = Plateau(max_x, max_y)
    mission = Mission(plateau)
    for idx in range(0, len(robot_data), 2):
        initial_x_position, initial_y_position, initial_direction = robot_data[idx].split()
        instructions = robot_data[idx + 1]
        mission.deploy_robot(int(initial_x_position), int(initial_y_position), initial_direction, instructions)
    results = mission.execute()
    for result in results:
        print(result)
