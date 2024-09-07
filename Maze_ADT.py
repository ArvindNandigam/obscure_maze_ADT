class Maze:
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.data = [['P'] * ncols for _ in range(nrows)]
        self.srow = None
        self.scol = None
        self.erow = None
        self.ecol = None

    def numRows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

    def setWall(self, rows, columns):
        for i in range(len(rows)):
            a = rows[i]
            b = columns[i]
            self.data[a][b] = "W"

    def setStart(self, row, column):
        self.srow = row
        self.scol = column
        self.data[row][column] = "S"

    def setExit(self, row, column):
        self.erow = row
        self.ecol = column
        self.data[row][column] = "E"

    def findPathMaze(self, a, b):
        s = self.data
        # Base cases
        if s[a][b] == "E":
            print("Way Found")
            return ["E"]
        elif s[a][b] == "W" or s[a][b] == "V":
            return []

        # Mark current cell as visited
        s[a][b] = "V"

        # Recursive exploration of adjacent cells
        for move in [("L", a, b-1), ("R", a, b+1), ("T", a-1, b), ("B", a+1, b)]:
            direction, row, col = move
            if 0 <= row < self.nrows and 0 <= col < self.ncols:
                path = self.findPathMaze(row, col)
                if path:
                    return [direction] + path
        return []
    def reset(self):
        self.data = [['P'] * self.ncols for _ in range(self.nrows)]

    def drawmaze(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                print(self.data[i][j].center(5, " "), end="")
            print()

m1 = Maze(10, 10)
m1.setStart(0, 0)
m1.setExit(0, 9)
m1.setWall([1,1,1,1,1,0,1,1], [1,2,3,4,5,6,7,8])
m1.drawmaze()
print(m1.findPathMaze(0, 0))

