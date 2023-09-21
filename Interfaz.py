from game2dboard import Board
import threading
import time

    
def mostrar(matriz, resultado) :
    rows = len(matriz)
    cols = len(matriz[0])

    b = Board( int(rows), int(cols) )
    b.title = "Laberinto"
    b.cell_size = 60
    b.cell_color = "white"
    b.grid_color= "blue"
    
    for i in range(rows) :
        for j in range(cols) :
            if matriz[i][j] == 1 :
                b[i][j] = "cuadro.png"
            if matriz[i][j] == 2 :
                b[i][j] = "cuadro3.png"
                
    aux = []
    for i in resultado :
        aux.append(i.split("\n"))
        
    for i in aux :
        i.remove("")
    
    aux2 = []
    for i in aux :
        for j in i :
            aux2.append(j)
    
    t = threading.Thread(target=timer, args=(aux2, b,))
    t.start()
    b.show()
        
    
def timer(aux, b) :
    for j in range(len(aux)) :
        r = aux[j].split(",")
        ranterior = aux[j - 1].split(",")
        b[int(r[1])][int(r[0])] = "cuadro2.png"
        b[int(ranterior[1])][int(ranterior[0])] = None
        time.sleep(0.25)
        
      
    
    