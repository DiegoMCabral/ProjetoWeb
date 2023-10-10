import random

# Define o número de vezes que o dado será jogado
num_jogadas = 6000

# Cria uma lista vazia para armazenar os resultados dos lançamentos
resultados = []

# Simula o lançamento do dado e armazena o resultado na lista
for i in range(num_jogadas):
    resultado = random.randint(1, 6)
    resultados.append(resultado)

# Imprime os resultados
print(resultados)
    