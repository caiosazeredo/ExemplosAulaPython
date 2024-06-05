#Entrada dos nomes
nomes_input = input("Digite cinco nomes, separados por virgula: ")
#conversão de lista para tupla
nomes = tuple(nomes_input.split(","))
#tratamento de erro/validação se foram inseridos 5 nomes
if len(nomes) != 5:
    #mensagem de erro
    print("Você não inseriu exatamente cinco nomes.")
else: # caso a entrada seja válida, ou seja, se foram inseridos 5 nomes
    # é feita a pergunta, de maneira análoga a um buscar de um site
    nome_inserido = input("Digite um nome para verificar se está na tupla: ")
    
    if nome_inserido in nomes:
        print("O nome está na tupla.")
    else:
        print("O nome não está na tupla.")
