from src.constants.constants import DIRECTIONS, LEFT_ROTATION, RIGHT_ROTATION


class Robot:
    def __init__(self, plateau, initial_x_position, initial_y_position, initial_direction, instructions):
        if initial_x_position < 0 or initial_x_position > plateau.max_x:
            raise ValueError(f"Invalid initial x position: {initial_x_position}")
        if initial_y_position < 0 or initial_y_position > plateau.max_y:
            raise ValueError(f"Invalid initial y position: {initial_y_position}")
        Robot.validate_instructions(instructions)
        self.x_position = initial_x_position
        self.y_position = initial_y_position
        self.direction = initial_direction
        self.plateau = plateau
        self.instructions = instructions

    def turn_left(self):
        self.direction = LEFT_ROTATION[self.direction]

    def turn_right(self):
        self.direction = RIGHT_ROTATION[self.direction]

    def move_forward(self):
        dx, dy = DIRECTIONS[self.direction]
        new_x, new_y = self.x_position + dx, self.y_position + dy
        if self.plateau.is_within_bounds(new_x, new_y):
            self.x_position = new_x
            self.y_position = new_y
        else:
            raise RuntimeError(f"Robot {self.direction} is out of bounds {new_x}, {new_y}")

    def execute_instructions(self):
        for instruction in self.instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'M':
                self.move_forward()

    def get_position(self):
        return f"{self.x_position} {self.y_position} {self.direction}"

    @staticmethod
    def validate_instructions(instructions):
        for instruction in instructions:
            if instruction not in ['L', 'R', 'M']:
                raise ValueError(f"Invalid instruction: {instruction}")
