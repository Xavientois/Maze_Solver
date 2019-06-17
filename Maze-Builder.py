import Solver
import turtle


# User Interface for designing maps for the pathfinding algorithm
# The user enters the pixel size of the tiles, and the width and height
# of the grid in tiles. Then, the turtle graphics window apears with a grid.
# the user left clicks to place and remove te starting point, the goal, and
# wall tiles. On right click, the maze draws the solution or prints that there
# is no path from start to goal.


# Makes a grid with gridlines with the passed parameters
# side --> Side of squares
# width --> Width of grid
# heigh --> Height of grid
def makeGrid(canvas, side, width, height):    
    canvas.delete('all')
    for x in range(width+1):
        canvas.create_line(x * side, 0, x * side, side * height, fill='white')
    for y in range(height+1):
        canvas.create_line(0, y * side, side * width, y * side, fill='white')
    canvas.config(scrollregion = canvas.bbox('all'))


# marks grid with walls, start, and goal
# coord --> coordinates to mark
# marking --> which marking to draw
def mark(coord, marking):
    canvas = t.screen.cv
    global startmark
    global goalmark
    if marking == 's':
        startmark = canvas.create_text(side * coord[0] + side / 2,
                                       side * coord[1] + side / 2, text='S',
                                       font=('Times', 22), fill='white')
    elif marking == 'g':
        goalmark = canvas.create_text(side * coord[0] + side / 2,
                                      side * coord[1] + side / 2, text='G',
                                      font=('Times', 22), fill='white')
    elif marking == '-s':
        canvas.delete(startmark)
    elif marking == '-g':
        canvas.delete(goalmark)
    elif marking == 1:
        walls[coord] = canvas.create_rectangle(side * coord[0], side * coord[1],
                                               side * coord[0] + side, side * coord[1] + side,
                                               fill='green')
    elif marking == 0:
        canvas.delete(walls[coord])
        del walls[coord]


# Turtle traces shortest path from s to g
# path --> List of coordinates through which to pass
def trace(path):
    t.goto(side * path[0][0] + side / 2, -1 * side * path[0][1] - side / 2)
    t.showturtle()
    t.clear()
    t.pendown()
    for coord in path:
        t.goto(side * coord[0] + side / 2, -1 * side * coord[1] - side / 2)


# handles click from user on grid
def click(x, y):
    x = int(x // side)
    y = int( -1 * (y // side + 1))
    coord = (x, y)
    global start
    global goal
    global walls

    if x < width and x > -1 and y < height and y > -1: # check if in grid
        if start == None and coord != goal:
            start = coord
            mark(coord, 's')
        elif goal == None and coord != start:
            goal = coord
            mark(coord, 'g')
        elif coord == start:
            start = None
            mark(coord, '-s')
        elif coord == goal:
            goal = None
            mark(coord, '-g')
        else :
            if coord in walls:
                mark(coord, 0)
            else:
                mark(coord, 1)


# handles right clck
def rclick(x, y):
    if start == None or goal == None:
        print('Please set start and goal points')
    else:
        solution = Solver.solve(start, goal, walls, height, width)
        if isinstance(solution, str):
            print(solution)
        else:
            trace(solution)

# runs the user's creation of the map
# t --> turtle
def designMap(t):
    t.screen.onclick(click) # map function to click on canvas
    t.screen.onclick(rclick, 2)
    t.screen.listen()
    
        
# main function to prompt user to input grid size and run UI
def main():
    global side
    global width
    global height
    side = input('Input tile size: ')
    width = input('Input grid width: ')
    height = input('Input grid height: ')
    # Set up Turtle and screen to draw grid
    global t
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(4) # Make the turtle super speedy
    t.pencolor("red")
    t.width(3)
    t.shape('turtle')
    t.clear()
    t.screen.bgcolor('black')
    t.screen.setup(side * width + side / 2, side * height + side / 2)
    makeGrid(t.screen.cv, side, width, height)

    global start
    global goal
    global walls
    start = None
    goal = None
    walls = {}

    designMap(t)
    turtle.mainloop()

main()
