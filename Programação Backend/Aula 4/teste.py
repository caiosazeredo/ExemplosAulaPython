print("Bem vindo ao Programa de Classificação")

lista_classificacion,lista_tempo = [], []

print("Digite o nome dos 7 primeiros pilotos e tempo da 6Q1")
for i in range(7):
    nome = input(f"Piloto {i+1}:")
    tempo = input(f"Tempo {i+1}:")
    lista_classificacion.append([nome])
    lista_tempo.append(tempo)
    print(f"O {i+1} lugar da 6Q1 ficou com {lista_classificacion[i]}no Tempo de {lista_tempo[i]}")

print(lista_classificacion,lista_tempo)

lista_classificacion1,lista_tempo1 = [], []

print("Digite o nome dos 5 primeiros pilotos e tempo da 6Q2 ")
for i in range(5):
    nome = input(f"Piloto {i+1}:")
    tempo = input(f"Tempo {i+1}:")
    lista_classificacion1.append([nome])
    lista_tempo1.append(tempo)
    print(f"O {i+1} lugar da 6Q2 ficou com {lista_classificacion1[i]}no Tempo de {lista_tempo1[i]}")

print(lista_classificacion1,lista_tempo1)

lista_classificacion2,lista_tempo2 = [], []

print("Digite o nome dos 3 primeiros pilotos e tempo da 6Q3 ")
for i in range(3):
    nome = input(f"Piloto {i+1}:")
    tempo = input(f"Tempo {i+1}:")
    lista_classificacion2.append([nome])
    lista_tempo2.append(tempo)
    print(f"O {i+1} lugar da 6Q3 ficou com {lista_classificacion2[i]}no Tempo de {lista_tempo2[i]}minutos")