import uuid

from src.constants.constants import DIRECTIONS, LEFT_ROTATION, RIGHT_ROTATION


class Robot:
    def __init__(self, plateau, initial_x_position, initial_y_position, initial_direction, instructions):
        print(f"Creating robot at {initial_x_position}, {initial_y_position}, facing {initial_direction}")

        if initial_x_position < 0:
            raise ValueError(f"Initial x position {initial_x_position} is below 0 (min bound).")
        if initial_x_position > plateau.max_x:
            raise ValueError(f"Initial x position {initial_x_position} exceeds plateau max_x {plateau.max_x}.")
        if initial_y_position < 0:
            raise ValueError(f"Initial y position {initial_y_position} is below 0 (min bound).")
        if initial_y_position > plateau.max_y:
            raise ValueError(f"Initial y position {initial_y_position} exceeds plateau max_y {plateau.max_y}.")

        Robot.validate_instructions(instructions)
        self.x_position = initial_x_position
        self.y_position = initial_y_position
        self.direction = initial_direction
        self.plateau = plateau
        self.instructions = instructions
        self.id = uuid.uuid4()

        print(f"[Robot {self.id} initialized.")

    def turn_left(self):
        print(f"Robot {self.id} turning left from {self.direction}")
        self.direction = LEFT_ROTATION[self.direction]
        print(f"Robot {self.id} now facing {self.direction}")

    def turn_right(self):
        print(f"Robot {self.id} turning right from {self.direction}")
        self.direction = RIGHT_ROTATION[self.direction]
        print(f"Robot {self.id} now facing {self.direction}")

    def move_forward(self):
        dx, dy = DIRECTIONS[self.direction]
        new_x, new_y = self.x_position + dx, self.y_position + dy
        print(
            f"Robot {self.id} attempting to move from ({self.x_position}, {self.y_position}) to ({new_x}, {new_y})")

        if self.plateau.is_within_bounds(new_x, new_y):
            self.x_position = new_x
            self.y_position = new_y
            print(f"Robot {self.id} moved to ({self.x_position}, {self.y_position})")
        else:
            raise RuntimeError(
                f"Robot {self.id} attempted to move out of bounds. "
                f"Direction: {self.direction}, Target: ({new_x}, {new_y})"
            )
    def execute_instructions(self):
        print(f"Executing instructions for Robot {self.id}: {self.instructions}")
        for instruction in self.instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'M':
                self.move_forward()
        print(f"Final position for Robot {self.id}: {self.get_position()}")

    def get_position(self):
        return f"{self.x_position} {self.y_position} {self.direction}"

    @staticmethod
    def validate_instructions(instructions):
        for instruction in instructions:
            if instruction not in ['L', 'R', 'M']:
                raise ValueError(f"Invalid instruction: {instruction}")
