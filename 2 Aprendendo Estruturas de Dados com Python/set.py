# Set é uma coleção que não possui objetos repetidos
conjunto = {1, 2, 3, 1, 3, 4}
print(set(conjunto)) # a ordem dos elementos pode variar

# Conjunto não suporta indexação e nem fatiamento, para isso tem que transformar em lista
# Posso iterar um set e usar enumurate

# Métodos
A = {1, 2, 3}
B = {2, 3, 4}

print(A.union(B)) # {1, 2, 3, 4}
A.intersection(B) # {2, 3}
A.difference(B) # {1}
A.symmetric_difference(B) # oposto da intersection ou (union menos intersection) {1,4}
A.issubset(B) # False -> Se todos os elementos de A então dentro do conjunto B
A.issuperset(B) # False -> Se todos os elementos de B então dentro do conjunto A
A.isdisjoint(B) # False -> Não tem elementos em intersection. True se não tem, False se tem.
A.add(3)
A.clear()
A.copy()
A.discard(1) # Descarta o valor 1 se tiver no conjunto
A.discard(45)
A.pop()
A.remove(0) # Se o elemento não existe, dá erro
len(A)
1 in B # False