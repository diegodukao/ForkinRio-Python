import re

def pega_dados(arquivo):
    for linha in arquivo:
        lista = re.findall('\w+', linha)
        yield tuple(lista)
    
def le_arquivo():
    arquivo = open('/home/diego/Documents/forkinrio/python-parte3/arquivo')
    for tupla in pega_dados(arquivo):
        if (len(tupla) > 0):
            print tupla
        
le_arquivo()
