def calculo():
    nota1 = float(input("Insira a primeira nota do aluno: "))
    nota2 = float(input("Insira a segunda nota do aluno: "))

    media = (nota1 + nota2)/2

    return media

def resultado():
    media = calculo()
    if(media >= 7):
        print(f"Aluno Aprovado - média: {media}")
    else:
        print(f"Aluno Reprovado - média: {media}")

if __name__ == '__main__':
    resultado()