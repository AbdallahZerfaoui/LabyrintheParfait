
class square(object):
    def __init__(self):
        self.UpperWall = 1
        self.LowerWall = 1
        self.RightWall = 1
        self.LeftWall = 1
        self.position = (0, 0)
        self.visited = 0

    def findUpperNeighbor(self, coord, Grid):
        (i, j) = coord
        if i != 0:
            return Grid()[i - 1][j]
        else:
            return None

    def findLowerNeighbor(self, coord, Grid):
        (i, j) = coord
        (n, p) = Grid.size
        if i != n - 1:
            return Grid()[i + 1][j]
        else:
            return None

    def findLeftNeighbor(self, coord, Grid):
        (i, j) = coord
        (n, p) = Grid.size
        if j != 0:
            return Grid()[i][j - 1]
        else:
            return None

    def findRightNeighbor(self, coord, Grid):
        (i, j) = coord
        (n, p) = Grid.size
        if j != p - 1:
            return Grid()[i][j + 1]
        else:
            return None