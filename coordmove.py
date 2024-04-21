def CreateGrid(width, height, char="."):
    newgrid = []
    for y in range(height):
        newgrid.append([char]*width)
    return newgrid

def PrintGrid(grid):
    for y in grid:
        line = ""
        for x in y:
            line += str(x) + " "
        print(line)

def GetCoord(grid, pos):
    x, y = pos
    return grid[y][x]

def SetCoord(grid, pos, new):
    x, y = pos
    grid[y][x] = new
    return grid
