MAX = 3

for intento in range(1, MAX + 1):
    usuario = input("usuario: ")
    clave = input("contraseña: ")

    if usuario == "alumno" and clave == "python123":
        print("bienvenido")
        break 

    print("credenciales incorrectas")
else:
    print("acceso bloquado")