# Especificar o nome do arquivo e as informações dos livros
nome_arquivo = 'livros.txt'
num_novos_livros = input("\nDeseja adicionar livros? (sim/não): ").lower()

with open(nome_arquivo, 'a') as arquivo:
    while num_novos_livros != "não" or "n" or "no" or "nao":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        arquivo.write(f"Título: {titulo}, Autor: {autor}\n")
        num_novos_livros = input("\nDeseja adicionar mais livros? (sim/não): ").lower()

print(f"\nNovas informações adicionadas ao arquivo '{nome_arquivo}'.\n")