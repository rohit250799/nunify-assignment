def solve_rc_robots(input_data):
    # Parsing the input
    lines = input_data.strip().split('\n')
    warehouse_dimensions = tuple(map(int, lines[0].split()))
    commands = lines[1:]

    """
    Direction mappings - underneath, N S E and W represent directions and are stored in a list. 
    These directional representations are mapped to their equivalent coordinates using a key-value 
    structure (dictionary) in python named 'moves'
    """

    directions = ['N', 'E', 'S', 'W']
    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
