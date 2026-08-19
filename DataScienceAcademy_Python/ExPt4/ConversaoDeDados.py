#String para Integer
numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f"String '{numero_em_texto}' para Inteiro: {numero_inteiro}")


#String para Float
numero_decimal_em_texto = "45.77"
numero_float = float(numero_decimal_em_texto)
print(f"Strin '{numero_decimal_em_texto}' para Float: {numero_float}")

#Número para String
num = 25
num_texto = str(num)
print(f"Inteiro {num} para String: '{num_texto}', Tipo: {type(num_texto)}")

#Convertendo entre estruturas de dados (lista para tupla)
lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico= set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)

print(f"Lista Original: {lista_com_duplicatas}")
print(f"Convertida para conjunto: {conjunto_unico}")
print(f"Convertida de volta para lista: {lista_sem_duplicatas}")
