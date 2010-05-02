def mostra_opcoes():
    print "1 - Celsius para Fahrenheit"
    print "2 - Fahrenheit para Celsius"

    opcao = input("Opcao: ")

    if opcao == 1:
        valor_em_celsius = input("Valor em Celsius: ")
        valor_em_fahrenheit = celsius_para_fahrenheit(valor_em_celsius)
        print "Valor em Fahrenheit: " + str(valor_em_fahrenheit)
    elif opcao == 2:
        valor_em_fahrenheit = input("Valor em Fahrenheit: ")
        valor_em_celsius = fahrenheit_para_celsius(valor_em_fahrenheit)
        print "Valor em Celsius: " + str(valor_em_celsius)
    else:
        print "Opcao invalida"
    
    return

def celsius_para_fahrenheit(valor_em_celsius):
    return (9.0 / 5.0 * valor_em_celsius) + 32
    
def fahrenheit_para_celsius(valor_em_fahrenheit):
    return (valor_em_fahrenheit - 32) * 5.0 / 9.0 
    
mostra_opcoes()
