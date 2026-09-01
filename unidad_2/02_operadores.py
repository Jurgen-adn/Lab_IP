operador = input("inserta un operador(+,-,*,/): ")

o1 = input("inserta el primer número: ")
o2 = input("inserta el segundo número: ")

resultado = o1 + operador + o2
resultado = eval(resultado)
print(resultado)