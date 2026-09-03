for numero in range(2, 101):
    primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
    if primo:
        print(numero)