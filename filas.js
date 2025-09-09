const r = 3, c = 3;
let TwoDArr = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
];
let arr = new Array(r*c);

// Guardar por filas
for(let x=0; x<r; x++){
  for(let y=0; y<c; y++){
    let k = x*c + y;
    arr[k] = TwoDArr[x][y];
  }
}

console.log("Bidimensional:");
TwoDArr.forEach(row => console.log(row.join(" ")));

console.log("\nUnidimensional (por filas):");
console.log(arr.join(" "));
