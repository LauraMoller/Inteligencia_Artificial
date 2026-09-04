# -------- For para lista
frutas = ['maçã', 'banana', 'cereja']
for fruta in frutas:
    print(f"- {fruta}")


## ------- For para Tuplas
cores = ('vermelho', 'verde', 'azul')
for cor in cores:
    print(cor)


## ------- For para dicionário
armario = {"Vestidos": 6, "Blusas": 21, "Calças": 5}

for chave, valor in armario.items():
    print(chave, ":", valor)


# ------ For com range
print("Contagem até 5: ")
for numero in range(6):
    print(numero)


# ------ While
contador = 5
print("Contagem Regressiva: ")
while contador > 0:
    print(contador)
    contador -= 1
