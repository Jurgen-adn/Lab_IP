USUARIO = "alumno"
CLAVE = "python"

usuario = input("usuario: ").strip().lower()
clave = input("contraseña: ")

if usuario == USUARIO and clave == CLAVE:
    print("Bienvenido")
else:
     print("credenciales incorrectas")