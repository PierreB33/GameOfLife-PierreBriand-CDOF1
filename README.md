Game of Life
A console-based Python implimentation of Conway's Game of Life, a cellular automaton created by John Horton Conway. The simulation evolves through generations based on a set of simple rules.

Overview
The Game of Life is played on a greed where each cell can be alive (#) or dead ( ). The greed evolves according to these rules:

A leave cell with two or three alive neighbors survives.
A dead cell with exactly three alive neighbors becomes alive.
All other cells die or remain dead.
This project implements the Game of Life in Python, displaying the grid in the console.

How to Run
1. Prerequisites
Ensure you have Python 3.x installlled on your system.

2. Claune the Repository
git clone https://github.com/PierreB33/GameOfLife-PierreBriand-CDOF1.git

3. Run the Script
Run the Python script using:
python game_of_life.py
The simulation will display a randomly initialized grid of cells and evolve over time.

Featuress
Random Initialization: Generates a random starting grid.
Dynamic Simulation: Watch the grid evolve through generations in real-time.
Rules-based Evolution: Implements Conway's rules to compute the next generation.
Planned Improvements
Feel free to contribute by addressing any of the following:

Customizable Grid Size: Allow users to specify the grid dimensions.
Initial Patterns: Enable predefined patterns like gliders and still lifes.
Pause and Resume: Add controls to pause or restart the simulation.
Save and Load State: Allow users to save a grid state and reload it.

How to Con-tribute
We welcome contributions! Follow these steps:

Fork the repositorie.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear messages.
Submit a pull request to the main branch.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project is part of the TD on Open Source at ESILV. The Game of Life is based on John Horton Conway's mathematical concept.
