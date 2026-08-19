numeros_input = input("Introduce números separados por espacios: ")
lista_numeros = [float(x) for x in numeros_input.split()]

suma_total = 0
for num in lista_numeros:
    suma_total += num

print(f"La suma de todos los elementos es: {suma_total}")
