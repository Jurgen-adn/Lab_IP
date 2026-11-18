while True:
    nombre = input("nombre: ").strip()
 #   print(nombre)
    if nombre and nombre.replace(" ", "").isalpha():
        print(nombre)
        break

    print("usa letras y no dejes el nombre vacio.")

nombre_normalizado = nombre.title()
print(f"Hola, {nombre_normalizado}")