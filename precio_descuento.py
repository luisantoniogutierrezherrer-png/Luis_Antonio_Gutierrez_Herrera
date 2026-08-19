precio = float(input("Introduce el precio total de la compra: "))

if precio <= 0:
    rango = "invalido"
elif precio <= 100:
    rango = "hasta_100"
elif precio <= 200:
    rango = "hasta_200"
elif precio <= 500:
    rango = "hasta_500"
else:
    rango = "mas_500"

match rango:
    case "hasta_100":
        final = precio * 0.95  # 5% descuento
        print(f"Descuento del 5%. Total: ${final:.2f}")
    case "hasta_200":
        final = precio * 0.90  # 10% descuento
        print(f"Descuento del 10%. Total: ${final:.2f}")
    case "hasta_500":
        final = precio * 0.85  # 15% descuento
        print(f"Descuento del 15%. Total: ${final:.2f}")
    case "mas_500":
        final = precio * 0.80  # 20% descuento
        print(f"Descuento del 20%. Total: ${final:.2f}")
    case _:
        print("Monto no válido.")