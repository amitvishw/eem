class Plateau:
    def __init__(self, max_x: int, max_y: int):
        print(f"Initializing Plateau with max_x={max_x}, max_y={max_y}")
        if max_x < 0:
            raise ValueError(f"Plateau max_x must be non-negative. Got: {max_x}")
        if max_y < 0:
            raise ValueError(f"Plateau max_y must be non-negative. Got: {max_y}")

        self.max_x = max_x
        self.max_y = max_y

        print(f"Plateau successfully created with dimensions: (0, 0) to ({self.max_x}, {self.max_y})")

    def is_within_bounds(self, x: int, y: int):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
