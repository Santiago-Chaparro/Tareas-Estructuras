public class Main {
    public static void main(String[] args) {
        int r = 3, c = 3;
        int[][] TwoDArr = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
        int[] arr = new int[r*c];

        // Guardar por filas
        for(int x=0; x<r; x++){
            for(int y=0; y<c; y++){
                int k = x*c + y;
                arr[k] = TwoDArr[x][y];
            }
        }

        System.out.println("Bidimensional:");
        for(int x=0; x<r; x++){
            for(int y=0; y<c; y++)
                System.out.print(TwoDArr[x][y] + " ");
            System.out.println();
        }

        System.out.println("\nUnidimensional (por filas):");
        for(int val : arr) System.out.print(val + " ");
    }
}

