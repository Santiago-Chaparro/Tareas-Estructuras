using System;

class Program {
    static void Main() {
        int[] unaLista = {523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
                          158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
                          94, 510, 221, 73, 999};

        for (int numPasada = unaLista.Length - 1; numPasada > 0; numPasada--) {
            for (int i = 0; i < numPasada; i++) {
                if (unaLista[i] > unaLista[i + 1]) {
                    int temp = unaLista[i];
                    unaLista[i] = unaLista[i + 1];
                    unaLista[i + 1] = temp;
                }
            }
        }

        foreach (int num in unaLista) {
            Console.Write(num + " ");
        }
    }
}
