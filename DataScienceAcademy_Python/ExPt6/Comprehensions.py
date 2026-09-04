# Estruturas construtoras sintáticas, sendo elas List Comprehension (gera listas), Set Comprehension (gera conjuntos), Dict Comprehension (gera dicionários) e Generator expression (gera iteradores)

# ------------------------
# Lista []
quadrados = [x ** 2 for x in range(10)]
print(f"\nQuadrados de 0 a 9: {quadrados}")

pares = [x for x in range(21) if x % 2 == 0]
print(f"Números pares de 0 a 20: {pares}")

# Dicionário {}
quadrados_dic = {x: x ** 2 for x in range(6)}
print(quadrados_dic)

# Conjuntos{} - Conjunto não envia os números duplicados - Deordenado
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4]}
print(quadrados_set)

#Generator Expression - Não existe um pra tupla, precisa ser convertido
gen = (x **2 for x in range(6))

quadrados_tuple = tuple(gen)
print(quadrados_tuple)

