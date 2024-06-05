# Especificar o nome do arquivo e o título do livro a ser buscado
nome_arquivo = 'livros.txt'
titulo_procurado = '1984'

# Tentar abrir o arquivo no modo de leitura e buscar o título
try:
    with open(nome_arquivo, 'r') as arquivo:
        encontrado = False
        for linha in arquivo:
            if titulo_procurado in linha:
                print(f"Livro encontrado: {linha.strip()}")
                encontrado = True
                break
        if not encontrado:
            print(f"O livro '{titulo_procurado}' não foi encontrado.")
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
