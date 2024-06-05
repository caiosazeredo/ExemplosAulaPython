# matrizes para armazenar os dados das classificatórias
nomes_classificatoria1, tempos_classificatoria1 = [], []
nomes_classificatoria2, tempos_classificatoria2 = [], []
nomes_classificatoria3, tempos_classificatoria3 = [], []

# Coletando dados para a primeira classificatória com 7 pilotos
print("Digite o nome e o melhor tempo dos 7 pilotos da primeira classificatória (nome:tempo):")
for i in range(3):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    nomes_classificatoria1.append(nome)
    tempos_classificatoria1.append(tempo)

# Coletando dados para a segunda classificatória com 5 pilotos
print("Digite o nome e o melhor tempo dos 5 pilotos da segunda classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    nomes_classificatoria2.append(nome)
    tempos_classificatoria2.append(tempo)

# Coletando dados para a terceira classificatória com 3 pilotos
print("Digite o nome e o melhor tempo dos 3 pilotos da terceira classificatória (nome:tempo):")
for i in range(2):
    entrada = input(f"Piloto {i+1}: ").split(":")
    nome = entrada[0]
    tempo = float(entrada[1])
    nomes_classificatoria3.append(nome)
    tempos_classificatoria3.append(tempo)

# Imprimindo as matrizes das classificatórias
print("\nResultados da Primeira Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria1:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria1:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Segunda Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria2:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria2:
    print(f"{tempo:.2f} segundos", end=", ")

print("\n\nResultados da Terceira Classificatória:")
print("Pilotos: ")
for nome in nomes_classificatoria3:
    print(nome, end=", ")
print("\nTempos: ")
for tempo in tempos_classificatoria3:
    print(f"{tempo:.2f} segundos", end=", ")
