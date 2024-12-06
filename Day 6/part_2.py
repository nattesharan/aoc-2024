def simulate_guard_path_with_obstruction(map_data, obstruction):

    # Direction vectors (dx, dy) for ^, >, v, < in order
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_symbols = ['^', '>', 'v', '<']

    # Parse the input map
    grid = [list(row) for row in map_data.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])

    # Find initial position and direction of the guard
    for y in range(height):
        for x in range(width):
            if grid[y][x] in direction_symbols:
                guard_pos = (x, y)
                direction = direction_symbols.index(grid[y][x])
                grid[y][x] = '.'  # Replace guard's starting symbol with open space
                break

    # Add the obstruction provided
    ox, oy = obstruction
    grid[oy][ox] = '#'

    # Track visited states (position + direction)
    visited_states = set()

    # Simulate the guard's movement
    while True:
        # Current position and facing direction
        x, y = guard_pos
        dx, dy = directions[direction]

        # Next position
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if not (0 <= nx < width and 0 <= ny < height):
            return False  # Guard leaves the map

        # Check if there's an obstacle
        if grid[ny][nx] == '#':
            # Turn right
            direction = (direction + 1) % 4
        else:
            # Move forward
            guard_pos = (nx, ny)

        # Record the current state
        state = (guard_pos, direction)
        if state in visited_states:
            return True  # Guard is in a loop

        visited_states.add(state)


def find_obstruction_positions(map_data, grid):
    # Parse the input map
    
    height = len(grid)
    width = len(grid[0])

    # Find the guard's starting position
    for y in range(height):
        for x in range(width):
            if grid[y][x] in ['^', '>', 'v', '<']:
                start_pos = (x, y)
                break

    # Test all possible positions for an obstruction
    valid_positions = []
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '.' and (x, y) != start_pos:
                print(f'Placing an obstruction at ({x},{y}) and checking if gaurd is in loop')
                if simulate_guard_path_with_obstruction(map_data, obstruction=(x, y)):
                    valid_positions.append((x, y))

    return valid_positions


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        grid = [list(row) for row in text.strip().split('\n')]
        valid_positions = find_obstruction_positions(text, grid)
        print(len(valid_positions))
