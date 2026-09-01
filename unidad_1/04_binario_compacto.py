numero = 8 # aqui se puede cambiar el valor de numero para convertir otro numero a binario
if numero == 0: print("0") # si el numero es 0, se imprime 0
binario = "" #comienza la cadena binario vacia
while numero > 0: # si el numero es mayor que 0 entra en un bucle que se repite hasta que el numero sea 0
    residuo = numero % 2 # se obtiene el residuo de la division del numero entre 2
    binario = str(residuo) + binario # se agrega el residuo al principio de la cadena binario
    numero = numero // 2 # se actualiza el valor de numero para la siguiente iteración
print(binario) # se imprime el valor final de la cadena binario, que contiene la representación binaria del numero original