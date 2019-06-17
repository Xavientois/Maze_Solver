from Tkinter import Tk

# Reads positions of start, goal, and walls, and solves for shortest path.
# Only vertical and horizontal movement is permitted, not diagonal.


# Stores the data for the squares in the grid
class Square():

    def __init__(self, coord, parent):
        self.coord = coord
        self.parent = parent
        if parent == None:
          self.start_dis = 0
        else:
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
    squares = list(openl.values())
    small = squares[0]
    for square in squares:
        if square.score() < small.score():
            small = square
    return small


# Returns a list of possible neighbor squares (not a wall or in closed list)
# sqr --> sqr around which to check
def neighbors(sqr):
    closedl[sqr.coord] = openl[sqr.coord] # move sqaure from open list to closed list
    del openl[sqr.coord]

    pneighbors = [(sqr.coord[0], sqr.coord[1] + 1),
                  (sqr.coord[0] + 1, sqr.coord[1]),
                  (sqr.coord[0], sqr.coord[1] - 1),
                  (sqr.coord[0] - 1, sqr.coord[1])]

    for neighbor in pneighbors:  # remove any illegal squares
        if (neighbor[1] < height and neighbor[1] > -1
        and neighbor[0] < width and  neighbor[0] > -1
        and not neighbor in walls
        and neighbor not in closedl):
            square = Square(neighbor, sqr) # generate neighbor square

            if neighbor == goal:
                return square
            elif (neighbor not in openl
            or square.score() < openl[neighbor].score()):
                openl[neighbor] = square

    if openl != {}:
        return neighbors(min_score())  # check the smallest square
    else:
        return None

# Returns list of coords to get from start to goal while avoiding walls
def path():
    end = neighbors(Square(start, None))

    if end == None:
        return 'No path found'
    else:
        path = [end.coord]

    while end.parent != None:
        path.insert(0, end.parent.coord)
        end = closedl[end.parent.coord]

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

    goal = goalin
    start = startin
    walls = wallsin
    width = widthin
    height = heightin
    openl = {start : Square(start, None)}
    closedl = {}
    return path()

