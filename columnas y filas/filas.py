
r = 3
c = 3

arr = [0] * r * c

TwoDArr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]  
k = 0
for x in range(r):
    for y in range(c):
        k = x * r + y
        arr[k] = TwoDArr[x][y]
        k = k + 1

print("Los elementos del array bidimensional son: ")
for row in TwoDArr:
    for ele in row:
        print(ele, end=" ")  
    print()  

print("\nLos elementos del array unidimensional son: ")

for x in range(r):
    for y in range(c):
        print((arr[x * r + y]), end=" ")
