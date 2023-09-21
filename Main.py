from MazeValidator import MazeValidator
import Interfaz 
import itertools
import copy
import tkinter as tk
import csv


class Main :
    def main() :
        
        file_read = csv.reader(open("archivo.csv"))
        maze = list(file_read)
        aux = [[int(i) for i in row] for row in maze]
        mazeE = aux
        
        nums = [1, 2, 3, 4]
        posibilidades = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0,-1]
        ]
        resultados = []
 
        permutations = list(itertools.permutations(nums))
        
        nueva_lista = copy.deepcopy(mazeE)
        
        
        entradaX, entradaY, salidaX, salidaY, contadorDeEntradasSalidas = Main.buscarEntradaSalida(mazeE)
        texto = ""
        
        laberinto = Main.validarLaberinto(mazeE)
        laberinto2 = Main.check_one_squares(mazeE)
        
        if contadorDeEntradasSalidas != 2 :
            print("El laberinto no cumple la condición de tener una entrada y una salida exclusivamente.")
        elif not laberinto and laberinto2:
            print("El laberinto no es valido.")   
        else :
            mazeValidator = MazeValidator()
            for i in permutations:    
                mazeE = copy.deepcopy(nueva_lista)
                (p, texto, final) = mazeValidator.solve(mazeE, entradaX, entradaY, salidaX, salidaY, posibilidades[i[0] - 1][0], posibilidades[i[0] - 1][1], posibilidades[i[1] - 1][0], posibilidades[i[1] - 1][1], posibilidades[i[2] - 1][0], posibilidades[i[2] - 1][1], posibilidades[i[3] - 1][0], posibilidades[i[3] - 1][1], texto, False)
                if  p :
                    # print("Se encontró una solución.")
                    existe = False
                    for a in resultados :
                        if a == texto :
                            existe = True
                    if existe != True:
                        resultados.append(texto)
                else :
                    print("No se encontró una solución.")
                texto = ""
                    
        contador = 1
        Interfaz.mostrar(aux, resultados)
        print("\nCaminos a tomar.")
        for a in resultados :
            print("\ncamino número " + str(contador))
            print(a)
            contador += 1
            
    def buscarEntradaSalida(maze) :
        # Buscar la entrada y salida
        
        entradaX = -1
        entradaY = -1
        salidaX = -1
        salidaY = -1
        contadorDeEntradasSalidas = 0
        for i in range( len(maze) ) :
            for j in range( len(maze[0]) ) :
                if ( ( ( i == 0 or i == len(maze) - 1 ) or ( j == 0 or j == len(maze[0]) - 1 ) )  and 
                    maze[i][j] == 0 ):
                    contadorDeEntradasSalidas += 1
                    
                    if contadorDeEntradasSalidas == 1 :
                        entradaX = i
                        entradaY = j
                    elif contadorDeEntradasSalidas == 2 :
                        salidaX = i
                        salidaY = j
                        
        return entradaX, entradaY, salidaX, salidaY, contadorDeEntradasSalidas
    
    def validarLaberinto(maze) :
        # Validar que el laberinto no contenga cuadrados en 0
        
        for i in range( len(maze) ) :
            for j in range( len(maze[0]) ) :
                if maze[i][j] == 0 and i < len(maze) - 1 and j < len(maze[0]) - 1 and j > 0:
                    if maze[i][j + 1] == 0 and maze[i + 1][j] == 0 and maze[i + 1][j + 1] == 0 :
                        return False
                    elif maze[i][j - 1] == 0 and maze[i + 1][j] == 0 and maze[i + 1][j - 1] == 0 :
                        return False
                elif i == len(maze) - 1 and j == len(maze[0]) - 1:
                    return True
    
    def check_one_squares (maze):
    # Obtener el número de filas y columnas de la matriz
        rows = len (maze)
        cols = len (maze [0])

        # Crear una matriz auxiliar del mismo tamaño que maze
        # Cada elemento de esta matriz representa el tamaño del cuadrado de ceros
        # que termina en esa posición
        aux = [ [0] * cols for _ in range (rows)]

        # Recorrer la matriz maze por filas y columnas
        for i in range (rows):
            for j in range (cols):
                # Si el elemento actual es cero, entonces actualizar el elemento correspondiente en aux
                if maze [i] [j] == 1:
                    # El tamaño del cuadrado de ceros es el mínimo entre el elemento superior, el izquierdo y el diagonal superior izquierdo, más uno
                    aux [i] [j] = 1 + min (aux [i-1] [j], aux [i] [j-1], aux [i-1] [j-1])
                    # Si el tamaño es mayor que uno, entonces hay un cuadrado de ceros en la matriz
                    if aux [i] [j] > 1:
                        return True

        # Si se recorrió toda la matriz sin encontrar un cuadrado de ceros, entonces retornar False
        return False

if __name__ == '__main__':
    Main.main()