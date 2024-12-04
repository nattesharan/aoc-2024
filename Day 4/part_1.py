def count_xmas_occurrences(grid):
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        """Check for the word 'XMAS' in the direction (dx, dy)."""
        word = "XMAS"
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),   # Right
        (0, -1),  # Left
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Diagonal Down-Right
        (-1, -1), # Diagonal Up-Left
        (1, -1),  # Diagonal Down-Left
        (-1, 1)   # Diagonal Up-Right
    ]

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search(x, y, dx, dy):
                    count += 1

    return count

# Example input grid


# Convert the grid into a list of lists


# Count occurrences of 'XMAS'


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        grid = text.split('\n')
        grid = [list(row) for row in grid]
        result = count_xmas_occurrences(grid)
    print(f"Total occurrences of 'XMAS': {result}")