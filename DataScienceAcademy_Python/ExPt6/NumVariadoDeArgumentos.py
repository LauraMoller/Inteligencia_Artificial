# *args -> passa um número variável de argumentos - é uma tupla
from EstruturasCondicionaisERepeticao import nome


def soma_numeros(*args):
    total = 0
    for numero in args:
        total += numero

    return total


print(f"Soma: {soma_numeros(1, 2, 3, 4)}")
print(f"Soma: {soma_numeros(10.5, 0.5)}")


# **kwargd -> argumentos de tamanho variável, ex: dicionário
def exibe_info_pessoal(**kwargs):
    print("Informações da Pessoa: ")
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")


exibe_info_pessoal(nome="Carla",
                   profissao="Engenheira de Dados",
                   hobby="Leitura")

exibe_info_pessoal(nome="Márcia",
                   idade = 35)
