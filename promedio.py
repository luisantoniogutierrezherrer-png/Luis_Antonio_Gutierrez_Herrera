# Programa para calcular el promedio de tres números

# Solicitar los tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calcular el promedio (se suman y se divide entre 3)
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado
print(f"El promedio de los tres números es: {promedio:.2f}")