def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quicksort(menores) + [pivote] + quicksort(mayores)

datos = [523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
         158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
         94, 510, 221, 73, 999]

print("Lista original:")
print(datos)
print("\nLista ordenada:")
print(quicksort(datos))