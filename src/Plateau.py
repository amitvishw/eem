class Plateau:
    def __init__(self, max_x: int, max_y: int):
        if max_x < 0 or max_y < 0:
            raise ValueError(f"Invalid plateau size: {max_x}, {max_y}")
        self.max_x = max_x
        self.max_y = max_y

    def is_within_bounds(self, x: int, y: int):
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
