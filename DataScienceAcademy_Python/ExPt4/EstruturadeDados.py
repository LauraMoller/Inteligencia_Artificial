#Listas -----------------------------------------------------------

frutas = ["Maçã", "Banana", "Laranja" , "uva"]
print(f"Lista de Frutas: {frutas}") #Imprime igual mostrado em frutas, com []

print(type(frutas)) #List

#Acessando um item pelo índice
print(f"A primeira fruta da lista é {frutas[0]}")
print(f"A última fruta da lista é {frutas[-1]}")

#Adicionando um item ao final da lista
frutas.append("Abacaxi")
print(f"Lista após adicionar 'Abacaxi': {frutas}")

#Removendo um item
frutas.remove("Laranja")
print(f"Lista após remover 'Laranja': {frutas}")

#Modificando um item
frutas[0] = "Morango"
print(f"Lista após modificar o primeiro item: {frutas}")

#Verificando o tamanho da lista
print(f"A lista tem {len(frutas)} frutas.")

#deletando lista
del frutas
# não irá mais funcionar print(frutas)

print("\n\n\n")


#Tuplas -------------------------------------------------------------------

coordenadas= (10.0, 20.5)
print(f"Tupla de coordenadas: {coordenadas}")

print(type(coordenadas))

#Acessando pelo índice
print(f"Coordenada X: {coordenadas[0]}")
print(f"Coordenada Y: {coordenadas[1]}")

#modificar uma tupla resultará em erro
#coordenadas[0] = 15.0

print("\n\n\n")


#Dicionários --------------------------------------------------------------

aluno = {
    "nome" : "Bob",
    "idade": 22,
    "curso": "Introdução à Python",
    "eh_aluno_ativo": True
}

print(f"Dicionário do Aluno: {aluno}") #Imprime em linha separando cada par por vírgula

print(type(aluno))

#Acessando um valor pela chave
print(f"Nome do aluno: {aluno['nome']}")
print(f"Curso: {aluno.get('curso')}") #Forma segura de acessar as chaves

#Adicionando um par chave-valor
aluno["cidade"] = "São Paulo"
print(f"Dicionário Atualizado: {aluno}")

#modificando um valor existente
aluno["idade"] = 23
print(f"Idade atualizada: {aluno}")

#Removendo um par de chave-valor
del aluno["eh_aluno_ativo"]
print(f"Dicionário após remover a chave 'eh_aluno_ativo': {aluno}")

print("\n\n\n")

#Conjuntos(Sets) ----------------------------------------------------------

numeros = {1, 2, 3, 4, 5,}
print(f"Conjunto de números (sem duplicatas): {numeros}")

print(type(numeros))

#Adicionando um item
numeros.add(6)
print(f"Após adicionar o valor 6: {numeros}")

#Removendo um item
numeros.remove(2)
print(f"Após remover o número 2: {numeros}")

#Operações com Conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

#União - Todos os elementos de amboos os conjuntos - não repete valores
uniao = conjunto_a.union(conjunto_b)
print(f"União entra A e B: {uniao}")

#Interseção - elementos que estão em ambos os conjuntos
intersecao = conjunto_a.intersection(conjunto_b)
print(f"Interseção entre A e B: {intersecao}")