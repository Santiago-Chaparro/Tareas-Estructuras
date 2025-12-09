#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

void limpiarPantalla() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

void pausa() {
    cout << "\nPresiona ENTER para continuar...";
    cin.ignore();
    cin.get();
}

void mostrarTablero(const vector<vector<char>>& t) {
    cout << "    0 1 2 3 4 5 6 7 8 9\n";
    for (int i = 0; i < 10; i++) {
        cout << i << " | ";
        for (int j = 0; j < 10; j++) {
            cout << t[i][j] << ' ';
        }
        cout << '\n';
    }
}

bool colocarBarco(vector<vector<char>>& t, int f, int c, char d, int tam) {
    if (d == 'h') {
        if (c + tam > 10) return false;
        for (int i = 0; i < tam; i++) if (t[f][c + i] != '.') return false;
        for (int i = 0; i < tam; i++) t[f][c + i] = '@';
    }
    else {
        if (f + tam > 10) return false;
        for (int i = 0; i < tam; i++) if (t[f + i][c] != '.') return false;
        for (int i = 0; i < tam; i++) t[f + i][c] = '@';
    }
    return true;
}

// agua = o
// acierto = X
bool disparar(vector<vector<char>>& tablero, vector<vector<char>>& visible, int f, int c) {
    if (tablero[f][c] == '@') {
        tablero[f][c] = 'X';
        visible[f][c] = 'X';
        return true;
    }
    else {
        if (visible[f][c] == '.')
            visible[f][c] = 'o';
        return false;
    }
}

bool gano(const vector<vector<char>>& t) {
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < 10; j++)
            if (t[i][j] == '@') return false;
    return true;
}

int main() {
    vector<int> barcos = { 5,4,3,3,2 };

    vector<vector<char>> t1(10, vector<char>(10, '.'));
    vector<vector<char>> t2(10, vector<char>(10, '.'));
    vector<vector<char>> v1(10, vector<char>(10, '.'));
    vector<vector<char>> v2(10, vector<char>(10, '.'));

    cout << "Batalla Naval\n";

    for (int jugador = 1; jugador <= 2; jugador++) {
        vector<vector<char>>& t = (jugador == 1 ? t1 : t2);

        for (int tam : barcos) {
            bool listo = false;
            while (!listo) {
                limpiarPantalla();
                cout << "Jugador " << jugador << "\nColoca barco de tam " << tam << "\n\n";
                mostrarTablero(t);

                int f, c;
                char d;
                cout << "\nFila y columna: ";
                cin >> f >> c;
                cout << "Direccion (h/v): ";
                cin >> d;

                if (colocarBarco(t, f, c, d, tam)) listo = true;
                else {
                    cout << "\nNo se pudo colocar. Intenta de nuevo.";
                    pausa();
                }
            }
        }
        limpiarPantalla();
        cout << "Jugador " << jugador << " termino de colocar barcos.\n";
        pausa();
    }

    int turno = 1;

    while (true) {
        limpiarPantalla();

        vector<vector<char>>& tablero = (turno == 1 ? t2 : t1);
        vector<vector<char>>& visible = (turno == 1 ? v1 : v2);

        cout << "Turno del Jugador " << turno << "\nTablero del oponente\n\n";
        mostrarTablero(visible);

        int f, c;
        cout << "\nIngresa fila y columna del disparo: ";
        cin >> f >> c;

        bool acierto = disparar(tablero, visible, f, c);

        limpiarPantalla();
        cout << "Resultado del disparo:\n\n";
        mostrarTablero(visible);
        cout << "\nFue " << (acierto ? "ACIERT0 (X)" : "AGUA (o)") << "\n";

        pausa();

        if (gano(tablero)) {
            limpiarPantalla();
            cout << "\n\nEl Jugador " << turno << " ha ganado!\n";
            break;
        }

        turno = (turno == 1 ? 2 : 1);
    }

    return 0;
}
