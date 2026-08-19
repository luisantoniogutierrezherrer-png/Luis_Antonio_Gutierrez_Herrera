a = int(input("Introduce el primer numero: "))
b = int(input("Introduce el segundo numero: "))

x = abs(a)
y = abs(b)

while y != 0:
    temporal = y
    y = x % y
    x = temporal

print(f"El Maximo Comun Divisor (MCD) es: {x}")
