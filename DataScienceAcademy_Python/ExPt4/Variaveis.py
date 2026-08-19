nome_completo = "Laura Möller" #String
idade = 20 # Integer
altura = 1.80 #Float
eh_estudante = True #Boolean

print(f"Meu nome é {nome_completo}, tenho {idade} anos e {altura} de altura.")
if eh_estudante:
    print(f"Sou estudante.")
else:
    print(f"Não sou estudante")

# Regras de nomenclatura: começar com letra ou _; não começar com número; conter apenas caracteres alfanuméricos e underscores (A-z, 0-9 e _); case-sensitive.

#Variáveis Globais
saudacao = "Olá, mundo"
nome = "Aluno DSA"

def minha_funcao():
    #Variável Local
    nome = "Ana"
    print(f"\nDentro da função: {nome}")
    print(f"Acessando vairável global de dentro da funcao: {saudacao}")

minha_funcao()

print(f"Fora da função: {saudacao}")
print(f"Fora da função: {nome}")