inicio = float(input("Introduce el primer termino (inicio): "))
diferencia = float(input("Introduce la diferencia comun: "))
terminos = int(input("¿Cuantos terminos deseas mostrar?: "))

if terminos > 0:
    termino_actual = inicio
    i = 1
    print("Secuencia aritmetica: ", end="")
    while True:
        print(termino_actual, end=" ")
        termino_actual += diferencia
        i += 1
        if i > terminos:
            break
    print()
else:
    print("La cantidad de terminos debe ser mayor a 0.")
