lista=[6, 24, 56, 20, 44] 
najveca_vrednost = lista[0]
najmanja_vrednost = lista[0]
for j in range(1, len(lista)): 
    if lista[j] > najveca_vrednost: 
        najveca_vrednost = lista[j]
for i in range(1, len(lista)): 
    if lista[i] < najmanja_vrednost: 
        najmanja_vrednost = lista[i] 
print(lista)
print("paran = " + str(najveca_vrednost))
print("neparan = " + str(najmanja_vrednost))