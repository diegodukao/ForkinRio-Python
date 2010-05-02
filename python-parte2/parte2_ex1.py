def le_arquivo(nome_do_arquivo):
    arquivo = open(nome_do_arquivo, 'r')
    linhas = arquivo.readlines()
    numero_linhas = len(linhas)
    numero_de_caracteres = 0
    numero_de_palavras = 0
    for linha in linhas:
        numero_de_caracteres += len(linha) - 1
        numero_de_palavras += 
