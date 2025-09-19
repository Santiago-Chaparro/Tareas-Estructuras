unaLista =  [523, 12, 874, 45, 678, 299, 1000, 3, 487, 920,
           158, 742, 61, 333, 891, 7, 456, 275, 640, 812,
           94, 510, 221, 73, 999]

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

ordenamientoBurbuja(unaLista)
print(unaLista)