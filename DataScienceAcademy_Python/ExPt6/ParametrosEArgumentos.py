def apresensentacao(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")


#Chamada simples
apresensentacao("Laura", 20)

#Chamada com argumentos nomeados
apresensentacao(idade=21, nome="Ana")



#Parâmetros com valores padrão (default)
def sauldacao_completa(nome, saudacao="Olá"): #nome obrigatório, saudacao opicional pois tem default
    print(f"{saudacao}, {nome}!")

sauldacao_completa("Lucas")
sauldacao_completa("Marcos", "oii")