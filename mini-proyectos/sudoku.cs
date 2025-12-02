using System;
using System.IO;

class S
{
    static Random r = new Random();
    static int[,] b = new int[9, 9];
    static int[,] f = new int[9, 9];
    static int lvl = 1; 
    static int w = 0;   
    static int life = 3;

    static void Main()
    {
        while (true)
        {
            Console.Clear();
            Console.WriteLine("=== SUDOKU ===");
            Console.WriteLine("(1) Nuevo juego");
            Console.WriteLine("(2) Cargar juego");
            Console.Write("Opción: ");
            string op = Console.ReadLine();

            if (op == "1")
            {
                NuevoSudoku();
                Jugar();
            }
            else if (op == "2")
            {
                if (Cargar()) 
                {
                    Jugar();
                }
                else
                {
                    Console.WriteLine("No se pudo cargar el archivo.");
                    Console.ReadKey();
                }
            }
        }
    }

    static void NuevoSudoku()
    {
        life = 3;
        GenerarBase();
        QuitarNum();
        Copiar();
    }

    static void GenerarBase()
    {
        int[,] g = {
            {1,2,3,4,5,6,7,8,9},
            {4,5,6,7,8,9,1,2,3},
            {7,8,9,1,2,3,4,5,6},
            {2,3,4,5,6,7,8,9,1},
            {5,6,7,8,9,1,2,3,4},
            {8,9,1,2,3,4,5,6,7},
            {3,4,5,6,7,8,9,1,2},
            {6,7,8,9,1,2,3,4,5},
            {9,1,2,3,4,5,6,7,8}
        };

        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                b[i, j] = g[i, j];

        Mezclar(b);
    }

    static void Mezclar(int[,] a)
    {
        for (int k = 0; k < 20; k++)
        {
            int x1 = r.Next(9);
            int x2 = r.Next(9);
            for (int i = 0; i < 9; i++)
            {
                int t = a[x1, i];
                a[x1, i] = a[x2, i];
                a[x2, i] = t;
            }
        }
    }

    static void QuitarNum()
    {
        int min = 36, max = 49;
        if (lvl == 2) { min = 32; max = 35; }
        if (lvl == 3) { min = 28; max = 31; }
        if (lvl == 4) { min = 24; max = 27; }
        if (lvl == 5) { min = 17; max = 23; }

        int keep = r.Next(min, max + 1);
        int remove = 81 - keep;

        for (int k = 0; k < remove; k++)
        {
            while (true)
            {
                int x = r.Next(9);
                int y = r.Next(9);
                if (b[x, y] != 0)
                {
                    b[x, y] = 0;
                    break;
                }
            }
        }
    }

    static void Copiar()
    {
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                f[i, j] = b[i, j];
    }

    static void Imprimir()
    {
        Console.WriteLine("Vidas: " + life + " | Nivel: " + lvl);
        for (int i = 0; i < 9; i++)
        {
            if (i % 3 == 0) Console.WriteLine("-------------------------");
            for (int j = 0; j < 9; j++)
            {
                if (j % 3 == 0) Console.Write("| ");
                Console.Write((f[i, j] == 0 ? "." : f[i, j].ToString()) + " ");
            }
            Console.WriteLine("|");
        }
        Console.WriteLine("-------------------------");
    }

    static void Jugar()
    {
        while (true)
        {
            Console.Clear();
            Imprimir();
            if (Ganaste())
            {
                w++;
                Console.WriteLine("¡Ganaste!");
                if (life == 3)
                {
                    life = 3; 
                }
                else life++;

                if (w == 5 && lvl < 5)
                {
                    lvl++;
                    w = 0;
                    Console.WriteLine("Subes de nivel!");
                }

                Console.ReadKey();
                NuevoSudoku();
            }

            if (life <= 0)
            {
                Console.WriteLine("Perdiste.");
                life = 3;
                Console.ReadKey();
                Environment.Exit(0);
            }

            Console.WriteLine("(1) Movimiento");
            Console.WriteLine("(2) Guardar");
            Console.WriteLine("(3) Salir");
            Console.Write("Opción: ");
            string op = Console.ReadLine();

            if (op == "1") Movimiento();
            else if (op == "2") Guardar();
            else if (op == "3") Environment.Exit(0);

        }
    }

    static void Movimiento()
    {
        Console.Write("Fila (1-9): ");
        int x = int.Parse(Console.ReadLine()) - 1;
        Console.Write("Columna (1-9): ");
        int y = int.Parse(Console.ReadLine()) - 1;
        Console.Write("Número (1-9): ");
        int n = int.Parse(Console.ReadLine());

        if (b[x, y] != 0)
        {
            Console.WriteLine("Esa casilla es fija.");
            Console.ReadKey();
            return;
        }

        if (Valido(x, y, n))
            f[x, y] = n;
        else
        {
            life--;
            Console.WriteLine("Incorrecto. Vidas: " + life);
            Console.ReadKey();
        }
    }

    static bool Valido(int x, int y, int n)
    {
        for (int i = 0; i < 9; i++)
            if (f[x, i] == n || f[i, y] == n)
                return false;

        int sx = (x / 3) * 3;
        int sy = (y / 3) * 3;
        for (int i = sx; i < sx + 3; i++)
            for (int j = sy; j < sy + 3; j++)
                if (f[i, j] == n)
                    return false;

        return true;
    }

    static bool Ganaste()
    {
        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                if (f[i, j] == 0)
                    return false;
        return true;
    }

    static void Guardar()
    {
        using (StreamWriter sw = new StreamWriter("save.txt"))
        {
            sw.WriteLine(lvl);
            sw.WriteLine(w);
            sw.WriteLine(life);

            for (int i = 0; i < 9; i++)
            {
                string line = "";
                for (int j = 0; j < 9; j++)
                    line += f[i, j] + " ";
                sw.WriteLine(line);
            }
        }
        Console.WriteLine("Guardado.");
        Console.ReadKey();
    }

    static bool Cargar()
    {
        if (!File.Exists("save.txt")) return false;

        string[] t = File.ReadAllLines("save.txt");
        int idx = 0;

        lvl = int.Parse(t[idx++]);
        w = int.Parse(t[idx++]);
        life = int.Parse(t[idx++]);

        for (int i = 0; i < 9; i++)
        {
            string[] p = t[idx++].Split(' ');
            for (int j = 0; j < 9; j++)
                f[i, j] = int.Parse(p[j]);
        }

        return true;
    }
}
