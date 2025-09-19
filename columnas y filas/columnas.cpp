#include <iostream>
using namespace std;

int main() {
    const int r = 3, c = 3;
    int TwoDArr[r][c] = { {1,2,3}, {4,5,6}, {7,8,9} };
    int arr[r*c];

    // Guardar por columnas
    int k = 0;
    for(int x=0; x<r; x++){
        for(int y=0; y<c; y++){
            k = y*r + x;
            arr[k] = TwoDArr[x][y];
        }
    }

    cout << "Bidimensional:\n";
    for(int x=0; x<r; x++){
        for(int y=0; y<c; y++)
            cout << TwoDArr[x][y] << " ";
        cout << endl;
    }

    cout << "\nUnidimensional (por columnas):\n";
    for(int i=0; i<r*c; i++) cout << arr[i] << " ";
}
