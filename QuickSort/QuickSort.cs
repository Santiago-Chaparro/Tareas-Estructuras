using System;

class Program
{
    static void QuickSort(int[] arr, int low, int high)
    {
        if (low >= high) return;
        int pivot = arr[low];
        int i = low + 1, j = high;

        while (i <= j)
        {
            while (i <= high && arr[i] <= pivot) i++;
            while (j > low && arr[j] > pivot) j--;
            if (i < j)
            {
                int temp = arr[i]; 
                arr[i] = arr[j]; 
                arr[j] = temp;
            }
        }
        int tempPivot = arr[low]; 
        arr[low] = arr[j]; 
        arr[j] = tempPivot;

        QuickSort(arr, low, j - 1);
        QuickSort(arr, j + 1, high);
    }

    static void Main()
    {
        int[] arr = {523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
                     158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
                     94, 510, 221, 73, 999};

        Console.WriteLine("Lista original:");
        Console.WriteLine(string.Join(" ", arr));

        QuickSort(arr, 0, arr.Length - 1);

        Console.WriteLine("\nLista ordenada:");
        Console.WriteLine(string.Join(" ", arr));
    }
}
