n = int(input("Introduce un número: "))
i = 2
while i*i<= int(n):
    if n % i == 0:
        print("No es primo")
        break
    else:
        print("primo")
        break
    i = i + 1
