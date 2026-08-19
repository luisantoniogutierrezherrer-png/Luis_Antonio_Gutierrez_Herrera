numero = float(input("Introduce un numero para calcular su raiz cuadrada: "))

if numero < 0:
    print("Error: No se puede calcular la raiz cuadrada de un numero negativo en los reales.")
else:
    raiz = numero ** 0.5
    print(f"La raiz cuadrada de {numero} es: {raiz}")
