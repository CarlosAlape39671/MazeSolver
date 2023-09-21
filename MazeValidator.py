class MazeValidator :
    def solve(self, maze, startX, startY, endX, endY, a, b, c, d, e, f, g, h, texto, p5) :
        rows = len(maze)
        colums = len(maze[0])
        
        # Verificar si estamos fuera de los límites o en una celda bloqueda
        if startY < 0 or startX < 0 or startX >= rows or startY >= colums or maze[startX][startY] == 1 :
            return (False, texto, False)
        
        # Verificar si hemos llegado a la salida
        if startX == endX and startY == endY :
            return (True, texto, True)
        
        # Marcar la celda como visitada
        if p5 == False :
            maze[startX][startY] = 1
            # texto = texto + "Marcar la posición " + str(startY) + "," + str(startX) +"\n"
            texto = texto + str(startY) + "," + str(startX) +"\n"
        
        # Explorar las cuatro direcciónes posibles
        # Las siguientes funciones if permiten verificar si ya termino uno de los caminos para no seguir recorriendo
        solve = self.solve
        (p1, texto, p5) = solve(maze, startX + a, startY + b, endX, endY, a, b, c, d, e, f, g, h, texto, p5)
        if p5 == True :
            return (True, texto, True)
        (p2, texto, p5) = solve(maze, startX + c, startY + d, endX, endY, a, b, c, d, e, f, g, h, texto, p5)
        if p5 == True :
            return (True, texto, True)
        (p3, texto, p5) = solve(maze, startX + e, startY + f, endX, endY, a, b, c, d, e, f, g, h, texto, p5)
        if p5 == True :
            return (True, texto, True)
        (p4, texto, p5) = solve(maze, startX + g, startY + h, endX, endY, a, b, c, d, e, f, g, h, texto, p5)
        if p5 == True :
            return (True, texto, True)
        
        if ( p1 or 
            p2 or 
            p3 or 
            p4 ):
            return (True, texto, False)
        
        if p5 == False :
            # Si ninguna dirección lleva a la solución, desmarcar la celda
            maze[startX][startY] = 0
            # texto = texto + "Marcar la posición " + str(startY) + "," + str(startX) +"\n"
            texto = texto + str(startY) + "," + str(startX) +"\n"
        
        return (False, texto, False)