from game2dboard import Board
import threading
import time

# rows = len(matriz)
# cols = len(matriz[0])

b = Board( 10, 10 )
b.title = "Laberinto"
b.cell_size = 60
b.cell_color = "white"
b.grid_color= "blue"
# a = "cuadro.png"
# a = timer

def timer():
    for i in range(10) :
        for j in range(10) :
            if i == j :
                b[i][j] = "cuadro.png"
                b[i-1][j-1] = None
                time.sleep(0.25)
            
t = threading.Thread(target=timer)
t.start()
b.show()