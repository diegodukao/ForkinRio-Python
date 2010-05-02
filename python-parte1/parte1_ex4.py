def soma_media_variacao(dicionario):
    soma = 0
    for v in dicionario.values():
        soma += v
    
    media = float(soma) / len(dicionario)
    print "soma = " + str(soma)
    print "media = " + str(media)
    
    return

dicionario = {1: 2, 2: 3, 4: 32, 'a': 134}
soma_media_variacao(dicionario)
