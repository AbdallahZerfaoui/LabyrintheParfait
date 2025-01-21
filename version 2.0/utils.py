import tkinter


def Window(Grid):
	"""
		Displays the grid G in a graphical window using Tkinter.

		Parameters:
			G (Grid): The grid object to be displayed. The grid should have a `size` attribute 
					and an `affiche()` method that returns a string representation of the grid.

		Returns:
			None
	"""
	(n,p)=Grid.size
	root=tkinter.Tk()

	text_widget=tkinter.Text(root, width=4*p+1, height=2*n+1)
	text_widget.insert(tkinter.END, Grid.affiche())
	text_widget.pack(side=tkinter.RIGHT,padx=10, pady=10)
	root.title("MonLabyrinthe"); root.update_idletasks()
	root.mainloop()
    
def CreateFile(Grid,file_path):
    """
    Saves the grid representation to a file.

    Parameters:
        G (Grid): The grid object to be saved. The grid should have an `affiche()` method 
                  that returns a string representation of the grid.
        file_path (str): The file path where the grid representation will be saved.

    Returns:
        None
    """
    file = open(file_path,'w')
    txt = Grid.affiche()
    file.write(txt)
    file.close()
    file = open(file_path,'r')
    
def NextSquare(Grid,coord, mur):
    
    (i,j), (a,b) = coord, mur
    (n,p)=Grid.size
    if a-2*i==3 and i!=n-1:                #savoir vers quel case aller
        case=Grid()[i][j].voisinB((i,j),Grid).position
        (i,j)=case
        return Grid()[i][j]
    if a-2*i==1 and i!=0:
        case=Grid()[i][j].voisinH((i,j),Grid).position
        (i,j)=case
        return Grid()[i][j]
    if a-2*i==2 and b-j==1 and j!=0:
        case=Grid()[i][j].voisinG((i,j),Grid).position
        (i,j)=case
        return Grid()[i][j]
    if a-2*i==2 and b-j==2 and j!=p-1:
        case=Grid()[i][j].voisinD((i,j),Grid).position
        (i,j)=case
        return Grid()[i][j]

def BreakWall(Grid,coord):
    (i,j)=coord
    (n,p)=Grid.size
    if i%2==1:
        if i!=(2*n+1):
            Grid()[int((i-1)/2)][j-1].MH=0
        if i==(2*n+1):
            Grid()[n-1][j-1].MB=0
           
    if i%2==0:
        if j<=p:
            Grid()[int((i-2)/2)][j-1].MG=0
        else:
            Grid()[int((i-2)/2)][j-2].MD=0

    Grid.ListeM.append((i,j))