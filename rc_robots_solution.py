def solve_rc_robots(input_data):
    
    # Parsing the input
    lines = input_data.strip().split('\n')
    warehouse_dimensions = tuple(map(int, lines[0].split())) #a tuple of integers representing the warehouse dimensions stored
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

    #helper function to help with rotation

    def rotation(current_direction, turning_direction):
        index = directions.index(current_direction)
        if turning_direction == 'L': index = (index - 1) % 4 #since indexes start from 0
        elif turning_direction == 'R': index = (index + 1) % 4
        return directions[index]

    #processing each robot in the warehouse:

    answers = []
    for i in range(0, len(commands), 2):
        #to find out the initial position and direction
        x, y, direction = commands[i].split()
        x, y = int(x), int(y)
        instructions = commands[i+1]

        for instruction in instructions:
            if instruction in 'LR': direction = rotation(direction, instruction)
            elif instruction == 'M':
                dx, dy = moves[direction]
                nx, ny = x + dx, y + dy 

                #ensuring robots staying within boundary limits
                if 0 <= nx <= warehouse_dimensions[0] and 0 <= ny <= warehouse_dimensions[1]:
                    x, y = nx, ny
        
            #storing the final position
        answers.append(f'{x} {y} {direction}')
    return '\n'.join(answers)




#To test the solve_rc_robots function with the given input:
input_data = """5 5
1 0 N
MMRMMLMMR
3 2 E
MLLMMRMM"""

def main():
    output = solve_rc_robots(input_data=input_data)
    print(output)
    return

if __name__ == "__main__":
    main()