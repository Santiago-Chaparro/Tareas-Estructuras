#include <iostream>
using namespace std;

int main() {
    int unaLista[] = {523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
                      158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
                      94, 510, 221, 73, 999};
    int n = sizeof(unaLista) / sizeof(unaLista[0]);

    for (int numPasada = n - 1; numPasada > 0; numPasada--) {
        for (int i = 0; i < numPasada; i++) {
            if (unaLista[i] > unaLista[i + 1]) {
                int temp = unaLista[i];
                unaLista[i] = unaLista[i + 1];
                unaLista[i + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << unaLista[i] << " ";
    }
    cout << endl;

    return 0;
}
