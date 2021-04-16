# -*- coding: utf-8 -*-

# ==============================================================================
#########################  LABYRINTHE : version A  ############################
# ==============================================================================
__author__  = "Abdallah ZERFAOUI"
__version__ = "1.0"
__date__    = "2011-12-10"
__usage__   = "Game"
################################################################################
from math import *
from random import *
import tkinter 

def Fenetre():
    (n,p)=G.size
    racine=tkinter.Tk()

    texte=tkinter.Text(racine, width=4*p+1, height=2*n+1)
    texte.insert(tkinter.END,G.affiche())
    texte.pack(side=tkinter.RIGHT,padx=10, pady=10)
    racine.title("MonLabyrinthe"); racine.update_idletasks()
    racine.mainloop()
    

def CreerFichier(G,chaine):
    abdallah=open(chaine,'w')
    txt=G.affiche()
    abdallah.write(txt)
    abdallah.close()
    abdallah=open(chaine,'r')
    

def CaseSuivante(g,coord, mur):
    
    (i,j), (a,b) = coord, mur
    (n,p)=g.size
    if a-2*i==3 and i!=n-1:                #savoir vers quel case aller
        case=g()[i][j].voisinB((i,j),g).position
        (i,j)=case
        return g()[i][j]
    if a-2*i==1 and i!=0:
        case=g()[i][j].voisinH((i,j),g).position
        (i,j)=case
        return g()[i][j]
    if a-2*i==2 and b-j==1 and j!=0:
        case=g()[i][j].voisinG((i,j),g).position
        (i,j)=case
        return g()[i][j]
    if a-2*i==2 and b-j==2 and j!=p-1:
        case=g()[i][j].voisinD((i,j),g).position
        (i,j)=case
        return g()[i][j]

def CasserMur(G,coord):
    (i,j)=coord
    (n,p)=G.size
    if i%2==1:
        if i!=(2*n+1):
            G()[int((i-1)/2)][j-1].MH=0
        if i==(2*n+1):
            G()[n-1][j-1].MB=0
           
    if i%2==0:
        if j<=p:
            G()[int((i-2)/2)][j-1].MG=0
        else:
            G()[int((i-2)/2)][j-2].MD=0

    G.ListeM.append((i,j))
#################################################################################
class memoire:
    def __init__(self):

        Liste=[]
        self.etat=Liste
#================================================================================
    def vide(self):
        if len(self.etat)==0:
            return True
        else:
            return False
       
#==============================================================================
    def memoriser(self,element):
        self.etat.append(element)
#==============================================================================
    def rappeler(self):
        if not self.vide():
            return self.etat[len(self.etat)-1]
        else:
            print ("TA LISTE EST VIDE")
#==============================================================================
    def depiler(self):
        if not self.vide:
            self.etat.remove(self.rappeler())
            
                
###############################################################################
class case(object):
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
        self.memory=memoire()
        
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
                if CaseSuivante(g,(i,j),mur).visited==0:
                    L1.append(mur)
            L=L1
            g()[i][j].visited=1         #dire que la case est visité
            
            for element in self.memory.etat:     #on verifie que L ne contient pas de mur donnant sur
                                                 #des cases deja visité
                if CaseSuivante(g,element[1],element[0]).visited==1:
                    self.memory.etat.remove(element)
            
            if len(L)==0:
                       
                if not self.memory.vide():
                    
                    self.position=self.memory.rappeler()[1]
                          
                    self.memory.depiler()
                    (i,j)=self.position
                else:
                    
                    fini=True
                    CasserMur(G,(2,1))
                    CasserMur(G,(2*n,p+1))
                    CreerFichier(G,'Labyrinthe.txt')
                    Fenetre()
            else:
                
                (a,b)=choice(L)             #choisir la direction
                
                CasserMur(g,(a,b))
                g.ListeM.append((a,b))
                
                for k in L:
                    if k != (a,b):
                        self.memory.memoriser([k,g()[i][j].position])                   
                (i,j)=CaseSuivante(g,(i,j),(a,b)).position   #changer de case
                g()[i][j].visited=1 
                self.position=(i,j)
################################# TEST CODE  ##################################
n=7
p=5

G=grid(n,p)
for i in range (n):
    for j in range(p):
        G()[i][j]=case()
        G()[i][j].position=(i,j)
        

Taupe=taupe()
Taupe.parcourir(G)
CasserMur(G,(2,1))#l'entrée
CasserMur(G,(2*n,p+1))#la sortie














