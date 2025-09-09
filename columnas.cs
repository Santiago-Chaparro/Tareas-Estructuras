using System;

class Program {
    static void Main() {
        int r = 3, c = 3;
        int[,] TwoDArr = { {1,2,3}, {4,5,6}, {7,8,9} };
        int[] arr = new int[r*c];

        // Guardar por columnas
        for(int x=0; x<r; x++){
            for(int y=0; y<c; y++){
                int k = y*r + x;
                arr[k] = TwoDArr[x,y];
            }
        }

        Console.WriteLine("Bidimensional:");
        for(int x=0; x<r; x++){
            for(int y=0; y<c; y++)
                Console.Write(TwoDArr[x,y] + " ");
            Console.WriteLine();
        }

        Console.WriteLine("\nUnidimensional (por columnas):");
        foreach(int val in arr) Console.Write(val + " ");
    }
}
