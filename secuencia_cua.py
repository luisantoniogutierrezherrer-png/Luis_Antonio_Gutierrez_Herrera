n = int(input("¿Cuantos numeros de la secuencia de cuadrados deseas generar?: "))

if n > 0:
    i = 1
    print("Secuencia: ", end="")
    while True:
        print(i * i, end=" ")
        i += 1
        if i > n:
            break
    print()
else:
    print("Por favor introduce un numero mayor a 0.")
