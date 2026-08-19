cantidad = int(input("¿Cuantos numeros vas a introducir?: "))
mayores = 0
menores = 0
iguales = 0

for i in range(cantidad):
    numero = float(input(f"Introduce el numero {i + 1}: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print(f"\nResultados:\nMayores a cero: {mayores}\nMenores a cero: {menores}\nIguales a cero: {iguales}")
