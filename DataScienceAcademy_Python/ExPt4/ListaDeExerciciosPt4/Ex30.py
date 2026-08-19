peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

IMC = peso / (altura*altura)

print(f"IMC = {format(IMC, '.2f')}")