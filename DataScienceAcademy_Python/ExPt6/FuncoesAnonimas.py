# Função Lambda - é uma pequena função anônima, ou seja, uma função que não possui um nome próprio

dobro = lambda x: x * 2
print(f"O dobro de 7 é {dobro(7)}")

# É possível combinar a expressão lambda com a função map()
# map -> aplica uma função a cada elemento de um iterável (lista, tupla, etc) e retorna um objeto map
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(f"Quadrados: {quadrados}")


# Filtrando os Resultados - filter
quadrados_pares = list(filter(lambda x: x%2 ==0, quadrados))
print(f"Quadrados Pares: {quadrados_pares}")