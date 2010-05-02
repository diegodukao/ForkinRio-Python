def inverte_palavras_da_frase(frase):
    import re
    regex_palavras = re.compile("[A-Za-z]+")
    regex_separadores = re.compile("[,.?! ]")
    
    frase = frase.replace(", ", ",")
    
    palavras = regex_palavras.findall(frase)
    separadores = regex_separadores.findall(frase)
    
    palavras_invertidas = ""
    for i in range(len(palavras)):
        palavras_invertidas += palavras[i][::-1] + separadores[i]
    
    string_final = palavras_invertidas.replace(",", ", ")
    
    return string_final

frase = input("frase: ")
print inverte_palavras_da_frase(frase)
