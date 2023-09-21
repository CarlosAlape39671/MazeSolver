public class Main {
    public static void main(String[] args) {
        int[][] maze = {
            {0, 1, 0, 0, 0},
            {0, 1, 0, 1, 0},
            {0, 0, 0, 0, 0},
            {0, 1, 1, 1, 0},
            {0, 0, 0, 1, 0}
        };

        MazeSolver mazeSolver = new MazeSolver();
        if (mazeSolver.solve(maze, 0, 0, 4, 4)) {
            System.out.println("Se encontró una solución.");
        } else {
            System.out.println("No se encontró una solución");
        }
    }
}