#include <iostream>
using namespace std;

void quicksort(int arr[], int low, int high) {
    if (low >= high) return;
    int pivot = arr[low];
    int i = low + 1, j = high;

    while (i <= j) {
        while (i <= high && arr[i] <= pivot) i++;
        while (j > low && arr[j] > pivot) j--;
        if (i < j) swap(arr[i], arr[j]);
    }
    swap(arr[low], arr[j]);

    quicksort(arr, low, j - 1);
    quicksort(arr, j + 1, high);
}

int main() {
    int arr[25] = {523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
                   158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
                   94, 510, 221, 73, 999};

    cout << "Lista original:\n";
    for (int i = 0; i < 25; i++) cout << arr[i] << " ";

    quicksort(arr, 0, 24);

    cout << "\n\nLista ordenada:\n";
    for (int i = 0; i < 25; i++) cout << arr[i] << " ";

    return 0;
}
