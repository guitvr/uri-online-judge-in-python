lista = [int(i) for i in str(input()).split()]

lista_ordenada = []
lista_ordenada.append(lista[0]) 

for i in lista[1:]:
    for j in range(len(lista_ordenada)):
        if i <= lista_ordenada[j]:
            lista_ordenada.insert(j, i)
            break
        elif j+1 == len(lista_ordenada):
            lista_ordenada.append(i)
        else:
            continue

for n in lista_ordenada:
    print(n)
print()
for n in lista:
    print(n)
