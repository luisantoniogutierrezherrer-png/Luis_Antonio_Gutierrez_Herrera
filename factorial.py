n = int(input("Introduce un número entero positivo: "))

if n < 0:
    print("El factorial de un número negativo no existe.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        
    print(f"El factorial de {n} es: {factorial}")
