from Tkinter import Tk
from tkFileDialog import askopenfilename

# Simple prototype implementation of the A* pathfinding algorithm
# The program reads the map data from a .txt file and prints the series
# of coordinates through which to pass to get from the start to the goal.
# Only vertical and horizontal movement is permitted, not diagonal.


# Stores the data for the squares in the grid
class Square():

    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent
        self.start_dis = manhattan(start, coord)
        self.goal_dis = manhattan(goal, coord)

    def score(self):
        return self.start_dis + self.goal_dis


# Calculates the manhattan distance between two points
# coord1 --> First coordinate
# coord2 --> Second coordinate
def manhattan(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


# Reads map data from file (From txt to array of numbers)
# Input files should be plaintext consisting of 0, 1, 2, 3, and spaces
# 0 represents a walkable tile
# 1 represents a wall tile
# 2 represents the starting point
# 3 represents the goal point
# rows must all be of same length
# directory --> Str of the file directory from which to read
def readgrid(directory):
    file = open(directory) # Open and read .txt file
    text = file.read()

    grid = text.splitlines() # Split up the rows

    for row in range(len(grid)):
        grid[row] = grid[row].split() # Break rows into individual numbers

    return grid


# Returns the coordinates of the first instance of a value in a grid
# val --> The value to search for in grid
def getCoords(val):
    for y in range(len(grid)):
        if val in grid[y]:
            return (grid[y].index(val), y)
    return False


# Returns a list of coordinates of all instances of val in a grid
# val --> The value to search for in grid
def getAllCoords(val):
    coords = []
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if val == grid[y][x]:
                 coords.append((x, y))
    return coords


# Returns the next square to check
def min_score():
    squares = openl.values()
    small = squares[0]
    for square in squares:
        if square.score() < small.score():
            small = square
    return small.coord


# Returns a list of possible neighbor squares (not a wall or in closed list)
# coord --> coordinates around which to check
def neighbors(coord):
    closedl[coord] = openl[coord] # move sqaure from open list to closed list
    del openl[coord]
    
    pneighbors = [(coord[0], coord[1] + 1), (coord[0] + 1, coord[1]),
                 (coord[0], coord[1] - 1), (coord[0] - 1, coord[1])]

    for neighbor in pneighbors:  # remove any illegal squares
        if (neighbor[1] < len(grid) and neighbor[1] > -1
        and neighbor[0] < len(grid[0]) and  neighbor[0] > -1
        and not neighbor in walls
        and not closedl.has_key(neighbor)):
            square = Square(neighbor, coord) # generate neighbor square
            
            if neighbor == goal:
                return square
            elif (not openl.has_key(neighbor)
            or square.score() < openl[neighbor].score()):
                openl[neighbor] = square

    if openl != {}:
        return neighbors(min_score())  # check the smallest square
    else:
        return None

# Returns list of coords to get from start to goal while avoiding walls
def path():
    end = neighbors(start)

    if end == None:
        return 'No path found'
    else:
        path = [end.coord]

    while end.parent != None:
        path.insert(0, end.parent)
        end = closedl[end.parent]

    return path

# Returns file directory from user prompt
def getFile():
    Tk().withdraw()
    filename = askopenfilename()
    return filename
    

# main function reads map file and runs program
def main():
    global grid
    global start
    global goal
    global walls
    global openl
    global closedl

    print('Input directory of map data file: ')
    directory = getFile()    
    
    grid = readgrid(directory)
    start = getCoords('2')
    goal = getCoords('3')
    walls = getAllCoords('1')
    openl = {start : Square(start, None)}
    closedl = {}
    print(path())

main()
