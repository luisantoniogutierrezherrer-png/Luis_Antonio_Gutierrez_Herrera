while True:
    print("\n--- CALCULADORA BASICA ---")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    operacion = input("Selecciona una opcion: ")
    
    n1 = float(input("Introduce el primer numero: "))
    n2 = float(input("Introduce el segundo numero: "))
    
    if operacion == '1':
        print(f"Resultado: {n1 + n2}")
    elif operacion == '2':
        print(f"Resultado: {n1 - n2}")
    elif operacion == '3':
        print(f"Resultado: {n1 * n2}")
    elif operacion == '4':
        if n2 != 0:
            print(f"Resultado: {n1 / n2}")
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opcion no valida.")
        
    opcion = input("¿Deseas realizar otra operacion? (s/n): ")
    if opcion.lower() != 's':
        print("Programa terminado.")
        break
