def testa_primos_1_100():
    print "1: False"
    
    for i in range(2, 101):
        eh_primo = verifica_se_eh_primo(i)
        print str(i) + ": " + str(eh_primo)

def verifica_se_eh_primo(numero):
    for divisor in range(numero - 1, 1, -1):
        if numero % divisor == 0:
            return False
    else:
        return True

testa_primos_1_100()
