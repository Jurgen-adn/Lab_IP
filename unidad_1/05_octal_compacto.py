numero = 25 # aqui se introduce el numero a convertir
if numero == 0: #aqui se hace la comprobacion de si el numero es 0, en cuyo caso se imprime 0
   print("0") #aqui se imprime 0
else: #aqui se hace la conversion a octal
   octal = "" #aqui se inicializa la variable octal como una cadena vacia
   while numero > 0: #aqui se hace un bucle mientras el numero sea mayor que 0
       residuo = numero % 8 #aqui se calcula el residuo de la division del numero entre 8
       octal = str(residuo) + octal #aqui se concatena el residuo a la variable octal
       numero = numero // 8 #aqui se hace la division entera del numero entre 8
   print(octal) #aqui se imprime el resultado de la conversion a octal