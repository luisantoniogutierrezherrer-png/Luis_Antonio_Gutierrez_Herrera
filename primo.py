numero = int(input("Introduce un numero entero positivo: "))

if numero <= 1:
    print(f"El numero {numero} no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
            
    if es_primo:
        print(f"El numero {numero} es primo.")
    else:
        print(f"El numero {numero} no es primo.")
