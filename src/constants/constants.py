# directions and their coordinate changes (dx, dy)
DIRECTIONS = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

# Left rotation mappings
LEFT_ROTATION = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}

# Right rotation mappings
RIGHT_ROTATION = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}
