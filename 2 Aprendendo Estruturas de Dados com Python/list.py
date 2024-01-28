# Listas aninhadas formam matrizes (tabelas)
matriz = [
    [1,'a',2],
    ['b',3,4],
    [6,5,'c']
          ]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento
print(matriz[::-1])

# Iterar
for item in matriz:
    print(item)

for indice, item in enumerate(matriz):
    print(f'{indice}: {item}')

# Compreensão de listas -> criar lista nova com base em lista existente usando um filtro ou a modificando
numeros = [1, 30, 21, 2, 9, 65, 34]
pares_not_list_comprehension  = []
for numero in numeros:
    if numero % 2 == 0:
        pares_not_list_comprehension.append(numero)
print(pares_not_list_comprehension)

pares_list_comprehension = [numero for numero in numeros if numero % 2 == 0] # mais performático
print(pares_list_comprehension)

# Métodos
lista = []
lista.append(1)
lista.append([40, 30, 20])
lista.clear()
lista2 = lista.copy()
print(id(lista), id(lista2))
matriz.count('a')
lista.extend(matriz) # adicionar vários elementos de uma vez só
lista.index('b') # primeira ocorrência de um elemento
lista.pop() # lista é pilha, entra por cima e sai por cima. Retira o último elemento
lista.pop(0) # dá para passar o indice que desejo retirar
lista.remove('c') # sempre o primeiro
lista.reverse() # espelhar
lista.sort() # ordenar alfabeticamente
lista.sort(reverse=True)
lista.sort(key=lambda x: len(x))
lista.sort(key=lambda x: len(x), reverse=True)
len(lista)
sorted(lista, key=lambda x: len(x), reverse=True)