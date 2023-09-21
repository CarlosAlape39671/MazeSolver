public class MazeSolver {
    public boolean solve(
        int[][] maze, 
        int startX, 
        int startY, 
        int endX, 
        int endY) {
        int rows = maze.length;
        int cols = maze[0].length;

        // Verificar si estamos fuera de los límites o en una celda bloqueda
        if (startX < 0 || startX >= cols || startY < 0 || startY >= rows || maze[startY][startX] == 1) {
            return false;    
        }

        // Verificar si hemos llegado a la salida
        if (startX == endX && startY == endY) {
            return true;
        }

        // Marcar la celda como visitada
        maze[startY][startX] = 1;
        System.out.println("Marcar la posición " + startY + "," + startX);

        // Explorar las cuatro direcciónes posibles
        if (solve(maze, startX + 1, startY, endX, endY) || 
            solve(maze, startX - 1, startY, endX, endY) ||
            solve(maze, startX, startY + 1, endX, endY) ||
            solve(maze, startX, startY - 1, endX, endY) ) {
            return true;
        }

        // Si ninguna dirección lleva a la solución, desmarcar la celda
        maze[startY][startX] = 0;
        System.out.println("Marcar la posición " + startY + "," + startX);

        return false;
    }
}
