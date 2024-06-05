while True:
    entrada = input("Digite cinco nomes separados por vírgulas: ")
    valores = entrada.split(",")

    if len(valores) == 5:
        nome_inserido = input("Digite um nome para verificar se está na tupla: ")
        if nome_inserido in valores:
            print("O nome está na tupla.")
            break
        else:
            print("O nome não está na tupla.")
            break
    else:
        print("Erro. Por favor, insira 5 nomes")