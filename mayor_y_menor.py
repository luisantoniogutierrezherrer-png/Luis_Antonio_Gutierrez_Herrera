numeros_input = input("Introduce números separados por espacios: ")
lista_numeros = [float(x) for x in numeros_input.split()]

if len(lista_numeros) == 0:
    print("No introdujiste ningún número.")
else:
    mayor = lista_numeros[0]
    menor = lista_numeros[0]
    
    for num in lista_numeros:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
            
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
