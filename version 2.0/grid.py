class grid(object):
    def __init__(self, col=1, row=1, none=None):

        self.size, self.none = (col, row), none
        self.reset()

        self.WallsList = []  # liste des walls cassable
        for i in range(2, 2 * col + 1, 2):
            self.WallsList.append((i, 1))
        for j in range(row):
            self.WallsList.append((1, j + 1))
        for i in range(2, 2 * col + 1, 2):
            self.WallsList.append((i, row + 1))
        for j in range(row):
            self.WallsList.append((2 * col + 1, j + 1))

    def __repr__(self):

        return "%s%s" % (type(self).__name__, (self.size + (self.none,)))

    def __eq__(self, obj):

        return repr(self) == repr(obj) and self() == obj()

    def __len__(self):

        return self.size[0] * self.size[1]

    def __call__(self, *items):

        return self.grid

    def __str__(self):

        cols, rows, grid = range(self.size[0]), range(self.size[1] - 1, -1, -1), self()
        width = 2 + max(len(str(item)) for item in sum(grid, [1]))  # max cell width

        mat = [[str(grid[col][row]).center(width) for col in cols] for row in rows]

        sepcol, seprow = "|", "%s+" % (("+%s" % ("-" * width)) * self.size[0])
        rows = ["\n%s%s%s\n" % (sepcol, sepcol.join(cols), sepcol) for cols in mat]
        return "%s%s%s" % (seprow, seprow.join(rows), seprow)

    def clone(self):
        return eval(repr(self), {type(self).__name__: type(self)})

    def reset(self):
        cols, rows = range(self.size[0]), range(self.size[1])
        self.grid = [[self.none for row in rows] for col in cols]
        return self.grid

    def display(self):
        chaine = ""
        (n, p) = self.size
        for i in range(n):  # general case
            for j in range(p):
                if self()[i][j].UpperWall == 1:
                    chaine += "+---"
                else:
                    chaine += "+   "
            chaine += "+\n"
            for j in range(p):
                if self()[i][j].LeftWall == 1:
                    chaine += "|   "
                else:
                    chaine += "    "

            if self()[i][p - 1].RightWall == 1:
                chaine += "|"
            chaine += "\n"
        for j in range(p):
            if self()[n - 1][j].LowerWall == 1:
                chaine += "+---"
            else:
                chaine += "+   "
        chaine += "+"

        return chaine
