# -*- coding: utf-8 -*-

# ==============================================================================
#########################  LABYRINTHE : version B  ############################
# ==============================================================================
__author__  = "Abdallah ZERFAOUI"
__version__ = "2.0"
__date__    = "2025-01-21"
__usage__   = "Game"
################################################################################

from math import *
from random import *
from memory import *
from utils import *
import tkinter 

            
                
###############################################################################
class square(object):
    def __init__(self):
        self.MH=1
        self.MB=1
        self.MD=1
        self.MG=1
        self.position=(0,0)
        self.visited=0
        
    def voisinH(self,coord,g):
        (i,j)=coord
        if i!=0:
            return g()[i-1][j]
        else:
            return None
        
    def voisinB(self,coord,g):
        (i,j)=coord
        (n,p)=g.size
        if i!=n-1:
            return g()[i+1][j]
        else:
            return None

    def voisinG(self,coord,g):
        (i,j)=coord
        (n,p)=g.size
        if j!=0:
            return g()[i][j-1]
        else:
            return None

    def voisinD(self,coord,g):
        (i,j)=coord
        (n,p)=g.size
        if j!=p-1:
            return g()[i][j+1]
        else:
            return None
            
################################################################################
class grid(object):
  # ----------------------------------------------------------------------------
    def __init__(self, col=1, row=1, none=None):
        
        self.size, self.none = (col, row), none; self.reset()
        
        self.ListeM=[]          #liste des murs cassable
        for i in range(2,2*col+1,2):
            self.ListeM.append((i,1))
        for j in range(row):
             self.ListeM.append((1,j+1))
        for i in range(2,2*col+1,2):
            self.ListeM.append((i,row+1))
        for j in range(row):
             self.ListeM.append((2*col+1,j+1))
                   
  # ----------------------------------------------------------------------------
    def __repr__(self):
   
        return "%s%s" % (type(self).__name__, (self.size + (self.none,)))
  # ----------------------------------------------------------------------------
    def __eq__(self, obj):
   
        return repr(self) == repr(obj) and self() == obj()  
   # ----------------------------------------------------------------------------
    def __len__(self):
   
        return self.size[0]*self.size[1]
  # ----------------------------------------------------------------------------
    def __call__(self, *items):
  
        return self.grid
  # ----------------------------------------------------------------------------
    def __str__(self):
   
        cols, rows, grid = range(self.size[0]), range(self.size[1]-1,-1,-1), self()
        width = 2 + max(len(str(item)) for item in sum(grid,[1])) # max cell width
        
        mat = [[str(grid[col][row]).center(width) for col in cols] for row in rows]
        
        sepcol, seprow = '|', "%s+" % (("+%s" % ('-' * width)) * self.size[0])
        rows = ["\n%s%s%s\n" % (sepcol, sepcol.join(cols), sepcol) for cols in mat]
        return "%s%s%s" % (seprow, seprow.join(rows), seprow)
  # ----------------------------------------------------------------------------
    def __getitem__(self, cell):

        return 'TODO' # TODO
  # ----------------------------------------------------------------------------
    def __setitem__(self, cell, item):
 
        return 'TODO' # TODO
  # ----------------------------------------------------------------------------
    def __delitem__(self, cell):

        return 'TODO' # TODO
  # ---------------------------------------------------------------------------
    def clone(self):
  
        return eval(repr(self), {type(self).__name__: type(self)})
   # ----------------------------------------------------------------------------
    def list(self):

        return 'TODO' # TODO
   # ----------------------------------------------------------------------------
    def dict(self):

        return 'TODO' # TODO
   # ----------------------------------------------------------------------------
    def reset(self):
   
        cols, rows = range(self.size[0]), range(self.size[1])
        self.grid = [[self.none for row in rows] for col in cols]; return self.grid
#======================================================================================
    def affiche(self):
        chaine=''
        (n,p)=self.size
        for i in range(n):              #cas general
            for j in range(p):
                if self()[i][j].MH==1:
                    chaine+='+---'
                else :
                    chaine+='+   '
            chaine+='+\n'
            for j in range(p):
                if self()[i][j].MG==1:
                    chaine+='|   '
                else:
                    chaine+='    '
                    
            if self()[i][p-1].MD==1:
                chaine+='|'
            chaine+='\n'
        for j in range(p):
                if self()[n-1][j].MB==1:
                    chaine+='+---'
                else :
                    chaine+='+   '
        chaine+='+'
        
        return chaine
###############################################################################
class taupe(object):
    def __init__(self):
        self.position=(1,1)
        self.memory=memory()
        
    def parcourir(self,g):
        
        L=[]
        (i,j)=self.position
        g()[i][j].visited=1         #dire que la case est visité
        mur=(0,0)
        (n,p)=g.size
        fini=False
        while not fini:
            liste=[(2*i+2,j+1),(2*i+2,j+2),(2*i+1,j+1),(2*i+3,j+1)]
            L=filter(lambda x: x not in g.ListeM,liste)
           
            L1=[]
            for mur in L:             #on verifie que L ne contient pas de mur donnant sur
                                    #des cases deja visité
                if NextSquare(g,(i,j),mur).visited==0:
                    L1.append(mur)
            L=L1
            g()[i][j].visited=1         #dire que la case est visité
            
            for element in self.memory.state:     #on verifie que L ne contient pas de mur donnant sur
                                                 #des cases deja visité
                if NextSquare(g,element[1],element[0]).visited==1:
                    self.memory.state.remove(element)
            
            if len(L)==0:
                       
                if not self.memory.is_empty():
                    
                    self.position=self.memory.get_last_state()[1]
                          
                    self.memory.pop_last_state()
                    (i,j)=self.position
                else:
                    
                    fini=True
                    BreakWall(G,(2,1))
                    BreakWall(G,(2*n,p+1))
                    CreateFile(G,'Labyrinthe.txt')
                    Window(G)
            else:
                
                (a,b)=choice(L)             #choisir la direction
                
                BreakWall(g,(a,b))
                g.ListeM.append((a,b))
                
                for k in L:
                    if k != (a,b):
                        self.memory.store_element([k,g()[i][j].position])                   
                (i,j)=NextSquare(g,(i,j),(a,b)).position   #changer de case
                g()[i][j].visited=1 
                self.position=(i,j)
################################# TEST CODE  ##################################

if __name__ == '__main__':
	n=20
	p=20

	G=grid(n,p)
	for i in range (n):
		for j in range(p):
			G()[i][j]=square()
			G()[i][j].position=(i,j)
			

	Taupe=taupe()
	Taupe.parcourir(G)
	BreakWall(G,(2,1))#l'entrée
	BreakWall(G,(2*n,p+1))#la sortie














