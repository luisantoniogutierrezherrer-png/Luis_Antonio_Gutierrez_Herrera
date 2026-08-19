suma = 0
contador = 0
print("Introduce 5 numeros positivos (un numero negativo dara fin al programa):")

while contador < 5:
    numero = float(input())
    if numero < 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    print(f"La media es: {suma / contador}")
else:
    print("No se introdujeron numeros positivos.")
