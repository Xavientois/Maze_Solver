# Maze_Solver

Hi folks!

This README outlines the information about my Maze Solving Program.

Currently, only the protype of the pathfinding algorithm is complete, but it seems to be working quite well.
The end goal of this project is for the user to be able to draw the maze when prompted and the program will draw
the most efficient solution to the maze.

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
