limite = int(input("Introduce el numero limite maximo: "))
i = 1
impares = 0

if limite >= 1:
    while True:
        if i % 2 != 0:
            impares += 1
        i += 1
        if i > limite:
            break

print(f"Hay {impares} numeros impares entre 1 y {limite}")
