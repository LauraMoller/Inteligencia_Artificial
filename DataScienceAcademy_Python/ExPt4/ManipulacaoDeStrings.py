# Concatenação
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

#Tamanho da String
frase = " Aprender Python é muito divertido! "
print(f"Tamanho da variável frase: {len(frase)}")

#Maiúsculas e Minúsculas
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")

#Remover espaços em branco do início e do fim
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: {frase_sem_espacos}")

#Substituir texto
print(f"Substituindo divertido por legal: {frase_sem_espacos.replace('divertido', 'legal')}")

#Fatiamento (Slicing) -> o índice python começa em zero
print("\n" + frase_sem_espacos)
print(f"o primeiro caractere: {frase_sem_espacos[0]}")
print(f"A palavra 'python': {frase_sem_espacos[9:15]}") #Do índice 9 ao 14