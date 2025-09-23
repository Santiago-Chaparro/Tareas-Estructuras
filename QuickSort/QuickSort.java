public class Main {
    public static void quicksort(int arr[], int low, int high) {
        if (low >= high) return;
        int pivot = arr[low];
        int i = low + 1, j = high;

        while (i <= j) {
            while (i <= high && arr[i] <= pivot) i++;
            while (j > low && arr[j] > pivot) j--;
            if (i < j) {
                int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
            }
        }
        int temp = arr[low]; arr[low] = arr[j]; arr[j] = temp;

        quicksort(arr, low, j - 1);
        quicksort(arr, j + 1, high);
    }

    public static void main(String[] args) {
        int arr[] = {523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
                     158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
                     94, 510, 221, 73, 999};

        System.out.println("Lista original:");
        for (int x : arr) System.out.print(x + " ");

        quicksort(arr, 0, arr.length - 1);

        System.out.println("\n\nLista ordenada:");
        for (int x : arr) System.out.print(x + " ");
    }
}
