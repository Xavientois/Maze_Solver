# Maze_Solver

Hey folks!

This README outlines the information about my Maze Solving Program.

The first complete version of the code is up. When prompted, input the dimensions of the grid and the width of the tiles in pixels. The turtle graphics window should appear and you can begin editing the map. Left click to place or remove the start point, goal point, and walls. Then, when you're done editing the map, right click and watch as the turtle runs the maze along the shortest path. The program is a simple implementation of the A* algorithm. This has been a great learning experience and has really gotten me used to the python language.

ver 0.1:
  - Prototype for algorithm functions as intended
  - Reads the map from a .txt file to determine the coordinates of walls, the starting point, and goal
  - Prints the series of coordinates it passes through to get to the goal from the start point
  - testgrid.txt is provided as an example and test case of the input that the prototype takes

ver 1:
  - First complete version of program
  - Two files, Maze-Builder runs UI, and Solver consumes the map data and produces shortest path from start to goal
  - Maze Builder allows user to place and remove start, goal, and walls, as well as drawing solution to maze
  - Solver consumes map data and produces list of coordinates for solution of maze
  
 Potential Additions:
  - Diagonal Movement
  - Different difficulty of terrain
  - Dynamic maze modification, where user can modify maze while turtle is solving it
  
 If you have any suggestions or want to mess around with the code in this repository feel free!
 
 X
