import random
import os
import time

def create_grid(rows, cols):
    return [[random.choice(['#', ' ']) for _ in range(cols)] for _ in range(rows)]

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(row))
    print()

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(1 for dx, dy in directions if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == '#')

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == '#' and neighbors in (2, 3):
                new_grid[x][y] = '#'
            elif grid[x][y] == ' ' and neighbors == 3:
                new_grid[x][y] = '#'
    return new_grid

def main():
    rows, cols = 20, 40
    grid = create_grid(rows, cols)
    while True:
        display_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
