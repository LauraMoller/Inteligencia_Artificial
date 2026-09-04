#----- Break (Sai do loop)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Buscando pelo número 5")

for numero in numeros:
    if numero == 5:
        print("Número 5 encontrado!")
        break

# -----
print("Imprimindo apenas os números ímpares")

for numero in numeros:
    if numero%2 == 0:
        continue
    print(numero)