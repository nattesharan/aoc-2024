def simulate_guard_path(grid):

    # Directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_symbols = ['^', '>', 'v', '<']

    # Parse the grid to find the guard's initial position and direction
    rows = len(grid)
    cols = len(grid[0])
    guard_pos = None
    guard_dir = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in direction_symbols:
                guard_pos = (r, c)
                guard_dir = direction_symbols.index(grid[r][c])
                break
        if guard_pos:
            break

    visited = set()
    visited.add(guard_pos)

    # Simulate the guard's movements
    while True:
        # Calculate the position in front of the guard
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        # Check if the guard is going out of bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if the position in front is an obstacle
        if grid[next_pos[0]][next_pos[1]] == '#':
            # Turn right: Update direction clockwise
            guard_dir = (guard_dir + 1) % 4
        else:
            # Move forward: Update position
            guard_pos = next_pos
            visited.add(guard_pos)

    return len(visited)


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        grid = [list(row) for row in text.strip().split('\n')]
        distinct_positions = simulate_guard_path(grid)
        print(distinct_positions)

