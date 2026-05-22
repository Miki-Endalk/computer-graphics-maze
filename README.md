# Maze Generator and Solver

This project generates and solves a rectangular maze using Python, Pygame, and OpenGL. The application visually demonstrates maze generation and pathfinding algorithms through animated rendering.

## Features

* Random maze generation using Depth First Search (DFS)
* Animated maze creation process
* Maze solving with backtracking visualization
* Start and end openings on opposite maze edges
* Real-time OpenGL rendering using Pygame
* Replayable solving animation

## Maze Generation

The maze is generated using a stack-based Depth First Search (DFS) algorithm. A virtual “mouse” begins at a random cell and explores neighboring cells. The algorithm randomly selects an unvisited neighbor, removes the wall between the two cells, and continues forward.

Visited cells are stored in a stack, allowing the algorithm to backtrack whenever it reaches a dead end. This process continues until every cell in the maze has been visited.

The resulting maze is considered a “perfect maze,” meaning:

* Every cell is reachable
* There is exactly one valid path between any two cells
* No isolated sections exist

## Maze Solving

The maze solver uses a backtracking algorithm to find a path from the left entrance to the right exit.

The solver:

1. Starts at the left opening
2. Explores valid neighboring cells
3. Stores the current path in a stack
4. Backtracks when a dead end is reached
5. Continues until the exit is found

### Visualization

* Red cells represent the active solution path
* Blue cells represent explored dead ends
* A bright red/yellow highlight indicates the final destination

## Technologies Used

* Python
* Pygame
* PyOpenGL

## Controls

* ESC → Exit the program
* SPACE → Replay the maze-solving animation

## Requirements

**Important**: Use Python version 3.12.x and follow these steps one by one:

1. **Create new venv with 3.12**:
```bash
py -3.12 -m venv .venv
```
2. **Activate using**:
```bash
.venv\Scripts\activate
```
3. **Install packages**:
```bash
python -m pip install pygame PyOpenGL PyOpenGL_accelerate
```
Now, you can run the code

## Demo Video

Here is a demo of the maze being generated and solved.

[![Watch the video](https://www.loom.com/share/4cd97f8fbfca4b33827bb940cd27b9be)](https://www.loom.com/share/4cd97f8fbfca4b33827bb940cd27b9be)