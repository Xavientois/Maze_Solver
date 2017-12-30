from Tkinter import Tk

# Reads positions of start, goal, and walls, and solves for shortest path.
# Only vertical and horizontal movement is permitted, not diagonal.


# Stores the data for the squares in the grid
class Square():

    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent
        self.start_dis = parent.start_dis + 1
        self.goal_dis = manhattan(goal, coord)

    def score(self):
        return self.start_dis + self.goal_dis


# Calculates the manhattan distance between two points
# coord1 --> First coordinate
# coord2 --> Second coordinate
def manhattan(coord1, coord2):
    return abs(coord2[0] - coord1[0]) + abs(coord2[1] - coord1[1])


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
        if (neighbor[1] < height and neighbor[1] > -1
        and neighbor[0] < width and  neighbor[0] > -1
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
    

# main function reads map data and runs program
def solve(startin, goalin, wallsin, heightin, widthin):
    global start
    global goal
    global walls
    global height
    global width
    global openl
    global closedl   
    
    start = startin
    goal = goalin
    walls = wallsin
    width = widthin
    height = heightin
    openl = {start : Square(start, None)}
    closedl = {}
    return path()

