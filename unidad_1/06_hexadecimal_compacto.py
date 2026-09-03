numero = 12 # aqui se introduce el numero a convertir
if numero == 0: #aqui se hace la comprobacion de si el numero es 0, en cuyo caso se imprime 0
    print("0") #aqui se imprime 0
hexadecimal = "" #aqui se inicializa la variable hexadecimal como una cadena vacia
while numero > 0: #aqui se hace un bucle mientras el numero sea mayor que 0
    residuo = numero % 16 #aqui se calcula el residuo de la division del numero entre 16
    valores = "0123456789ABCDEF" #aqui se define una cadena con los valores hexadecimales
    hexadecimal = valores[residuo] + hexadecimal #aqui se concatena el valor correspondiente al residuo a la variable hexadecimal
    numero = numero // 16 #aqui se hace la division entera del numero entre 16
print(hexadecimal) #aqui se imprime el resultado de la conversion a hexadecimal