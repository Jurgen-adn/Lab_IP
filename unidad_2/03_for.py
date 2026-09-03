#for con rangos 
for numero in range(1, 6):
    cuadrado = numero ** 2
    print(numero, cuadrado)

#for con listas
materias = ["python", "linux", "interfaces"]

for posicion, materia in enumerate(materias):
    print(f"[{posicion}, {materia}]")

#for con cadenas
for materia in materias:
    print(materia)
    cadena = "0123456789ABCDEF"
    for letra in cadena:
        print(letra)
        
# for con 
for i in range (len(cadena)):
    print(cadena[i])