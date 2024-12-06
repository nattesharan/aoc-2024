# def parse_map(input_map):
#     grid = [list(row) for row in input_map.strip().split("\n")]
#     for y, row in enumerate(grid):
#         for x, cell in enumerate(row):
#             if cell in "^>v<":
#                 return grid, (x, y), cell
#     return grid, None, None

# def turn_right(direction):
#     directions = "^>v<"
#     return directions[(directions.index(direction) + 1) % 4]

# def move_forward(position, direction):
#     x, y = position
#     if direction == "^":
#         return (x, y - 1)
#     elif direction == ">":
#         return (x + 1, y)
#     elif direction == "v":
#         return (x, y + 1)
#     elif direction == "<":
#         return (x - 1, y)

# def simulate_guard(grid, start_pos, start_dir):
#     visited = set()
#     direction = start_dir
#     position = start_pos

#     while True:
#         visited.add(position)

#         # Calculate the next position
#         next_position = move_forward(position, direction)

#         # Check if the guard is out of bounds
#         x, y = next_position
#         if not (0 <= y < len(grid) and 0 <= x < len(grid[0])):
#             break

#         # Check for obstacles
#         if grid[y][x] == "#":
#             direction = turn_right(direction)
#         else:
#             position = next_position

#     return visited

# def count_distinct_positions(input_map):
#     grid, start_pos, start_dir = parse_map(input_map)
#     visited_positions = simulate_guard(grid, start_pos, start_dir)
#     return len(visited_positions)


# if __name__ == '__main__':
#     with open('input.txt') as f:
#         text = f.read()
#         result = count_distinct_positions(text)
#         print("Distinct positions visited:", result)

def simulate_guard_path(grid):

    # Direction vectors (dx, dy) for ^, >, v, < in order
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_symbols = ['^', '>', 'v', '<']

    # Parse the input map
    
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

    # Track visited positions
    visited = set()
    visited.add(guard_pos)

    # Simulate the guard's movement
    while True:
        # Current position and facing direction
        x, y = guard_pos
        dx, dy = directions[direction]

        # Next position
        nx, ny = x + dx, y + dy

        # Check if the next position is out of bounds
        if not (0 <= nx < width and 0 <= ny < height):
            break

        # Check if there's an obstacle
        if grid[ny][nx] == '#':
            # Turn right
            direction = (direction + 1) % 4
        else:
            # Move forward
            guard_pos = (nx, ny)
            visited.add(guard_pos)

    return len(visited)


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        grid = [list(row) for row in text.strip().split('\n')]
        distinct_positions = simulate_guard_path(grid)
        print(distinct_positions)

