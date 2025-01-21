import random
import os
import time

# Create a grid with random cells being either alive ('#') or dead (' ')
def create_grid(rows, cols):
    return [[random.choice(['#', ' ']) for _ in range(cols)] for _ in range(rows)]

# Clear the console and display the current state of the grid
def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows ('cls') or Unix-based systems ('clear')
    for row in grid:
        print(''.join(row))  # Print each row as a string
    print()

# Count the number of alive neighbors around a given cell
def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    # Define relative positions of the 8 possible neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum(1 for dx, dy in directions 
               if 0 <= x + dx < rows and 0 <= y + dy < cols and grid[x + dx][y + dy] == '#')

# Generate the next generation of the grid based on the rules of Conway's Game of Life
def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    # Create a new grid initialized with dead cells
    new_grid = [[' ' for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            neighbors = count_neighbors(grid, x, y)  # Count alive neighbors
            if grid[x][y] == '#' and neighbors in (2, 3):  # Survival rule
                new_grid[x][y] = '#'
            elif grid[x][y] == ' ' and neighbors == 3:  # Birth rule
                new_grid[x][y] = '#'
    return new_grid

# Main function to initialize and run the simulation
def main():
    rows, cols = 20, 40  # Dimensions of the grid
    grid = create_grid(rows, cols)  # Initialize the grid
    while True:
        display_grid(grid)  # Display the current state of the grid
        grid = next_generation(grid)  # Update the grid to the next generation
        time.sleep(0.5)  # Pause for 0.5 seconds between generations

# Entry point of the program
if __name__ == "__main__":
    main()

