from memory import memory
from random import choice
from utils import *

class taupe(object):
    def __init__(self):
        self.position = (1, 1)
        self.memory = memory()

    def explore(self, Grid):

        L = []
        (i, j) = self.position
        Grid()[i][j].visited = 1  # dire que la case est visité
        wall = (0, 0)
        (n, p) = Grid.size
        done = False
        while not done:
            liste = [
                (2 * i + 2, j + 1),
                (2 * i + 2, j + 2),
                (2 * i + 1, j + 1),
                (2 * i + 3, j + 1),
            ]
            L = filter(lambda x: x not in Grid.WallsList, liste)

            L1 = []
            for wall in L:  # on verifie que L ne contient pas de wall donnant sur
                # des cases deja visité
                if NextSquare(Grid, (i, j), wall).visited == 0:
                    L1.append(wall)
            L = L1
            Grid()[i][j].visited = 1  # dire que la case est visité

            for (
                element
            ) in (
                self.memory.state
            ):  # on verifie que L ne contient pas de wall donnant sur
                # des cases deja visité
                if NextSquare(Grid, element[1], element[0]).visited == 1:
                    self.memory.state.remove(element)

            if len(L) == 0:

                if not self.memory.is_empty():

                    self.position = self.memory.get_last_state()[1]

                    self.memory.pop_last_state()
                    (i, j) = self.position
                else:

                    done = True
                    BreakWall(Grid, (2, 1))
                    BreakWall(Grid, (2 * n, p + 1))
                    CreateFile(Grid, "Labyrinthe.txt")
                    Window(Grid)
            else:

                (a, b) = choice(L)  # choisir la direction

                BreakWall(Grid, (a, b))
                Grid.WallsList.append((a, b))

                for k in L:
                    if k != (a, b):
                        self.memory.store_element([k, Grid()[i][j].position])
                (i, j) = NextSquare(Grid, (i, j), (a, b)).position  # changer de case
                Grid()[i][j].visited = 1
                self.position = (i, j)