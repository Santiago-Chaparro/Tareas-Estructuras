function quicksort(arr) {
    if (arr.length <= 1) return arr;
    let pivot = arr[0];
    let menores = arr.slice(1).filter(x => x <= pivot);
    let mayores = arr.slice(1).filter(x => x > pivot);
    return [...quicksort(menores), pivot, ...quicksort(mayores)];
}

let arr = [523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
           158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
           94, 510, 221, 73, 999];

console.log("Lista original:");
console.log(arr);

console.log("\nLista ordenada:");
console.log(quicksort(arr));
