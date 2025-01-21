# -*- coding: utf-8 -*-

# ==============================================================================
#########################  LABYRINTHE : version B  ############################
# ==============================================================================
__author__ = "Abdallah ZERFAOUI"
__version__ = "2.0"
__date__ = "2025-01-21"
__usage__ = "Game"
################################################################################

from math import *
from random import *
from memory import *
from square import *
from taupe import *
from grid import *
from utils import *
import tkinter

if __name__ == "__main__":
    n = 20
    p = 20
    Grid = grid(n, p)
    for i in range(n):
        for j in range(p):
            Grid()[i][j] = square()
            Grid()[i][j].position = (i, j)
    Taupe = taupe()
    Taupe.explore(Grid)
    BreakWall(Grid, (2, 1))         # the entrance
    BreakWall(Grid, (2 * n, p + 1)) # the exit