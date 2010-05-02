def eh_primo(numero):
    for divisor in range(numero - 1, 1, -1):
        if numero % divisor == 0:
            return False
    return True

def gen_primos(n):
    i = 1
    while True:
        i += 1
        if eh_primo(i):
            yield i
        
        if i == n:
            return

for primo in gen_primos(100):
    print primo
