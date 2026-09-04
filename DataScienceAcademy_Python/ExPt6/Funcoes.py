# Função Simples
def saudacao():
    """Essa função exibe uma saudação"""  #---Equivale ao comentário /**/ do java
    print("\nOlá, seja bem vindo(a)!")

saudacao()


# Função com retorno
def soma(a, b):
    """Essa função retorna a soma de dois valores"""
    return a+b

resultado = soma(3,5)
print(f"O resultado da soma de 3 e 5 é {resultado}")

