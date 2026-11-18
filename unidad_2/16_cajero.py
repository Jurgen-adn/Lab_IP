def consultar_saldo():
    print("saldo: $0.00")
def depositar():
    print("deposito realizado")
def retirar():
    print("retiro realizado")
def salir():
    print("saliendo del cajero automatico")
def mostrar_menu():
    print("bienvenido al cajero automatico")
    print("1. consultar saldo")
    print("2. depositar")
    print("3. retirar")
    print("4. salir")
    return input("opcion: ").strip()
def main():
        while True:
            opcion = mostrar_menu()

            if opcion == "1":
              consultar_saldo()
            elif opcion == "2":
              depositar()
            elif opcion == "3":
              retirar()
            elif opcion == "4":
              salir()
              break
            else:
             print("opcion invalida")

main()