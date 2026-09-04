numeros = (3, 7, 10, 15, 20)

for n in numeros:
    if n%2 ==0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")



#----------
nomes = ["Ana", "Bruno", "Carlos", "Amanda", "Beatriz"]

for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome encontrado com A: {nome}")


#--------
produtos = {"Arroz":25, "Feijão": 12, "Carne": 45, "Macarrão" : 8}

for item,preco in produtos.items():
    if preco > 20:
        print(f"{item} custa {preco} reais (acima de 20)")
