numeros_input = input("Introduce números separados por espacios: ")
lista_numeros = [int(x) for x in numeros_input.split()]

pares = 0
impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
