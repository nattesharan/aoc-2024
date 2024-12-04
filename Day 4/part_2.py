def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    # Iterate through each cell as the center of the X
    for i in range(0, rows - 1):
        for j in range(0, cols - 1):
            # Check for the forward "MAS" pattern (top left -> bottom right)
            if (grid[i-1][j-1] == 'M' and grid[i][j] == 'A' and grid[i+1][j+1] == 'S' and
                grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                count += 1

            # Check for the backward "MAS" pattern (top right -> bottom left)
            if (grid[i-1][j+1] == 'S' and grid[i][j] == 'A' and grid[i+1][j-1] == 'M' and
                grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M'):
                count += 1

    return count
# Count occurrences of 'X-MAS'


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        grid = text.split('\n')
        grid = [list(row) for row in grid]
        result = count_x_mas(grid)
        print(f"Total occurrences of 'X-MAS': {result}")