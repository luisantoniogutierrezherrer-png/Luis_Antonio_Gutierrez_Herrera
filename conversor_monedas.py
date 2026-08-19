pesos = float(input("Introduce la cantidad en pesos mexicanos (MXN): "))

print("Monedas disponibles: USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS")
destino = input("¿A qué moneda deseas convertir?: ").upper()

match destino:
    case "USD": print(f"Total: {pesos * 0.059:.2f} USD")
    case "EUR": print(f"Total: {pesos * 0.054:.2f} EUR")
    case "THB": print(f"Total: {pesos * 2.10:.2f} THB")
    case "JPY": print(f"Total: {pesos * 8.58:.2f} JPY")
    case "KRW": print(f"Total: {pesos * 78.50:.2f} KRW")
    case "AUD": print(f"Total: {pesos * 0.090:.2f} AUD")
    case "PEN": print(f"Total: {pesos * 0.22:.2f} PEN")
    case "CAD": print(f"Total: {pesos * 0.080:.2f} CAD")
    case "VES": print(f"Total: {pesos * 2.15:.2f} VES")
    case "ARS": print(f"Total: {pesos * 50.30:.2f} ARS")
    case _: print("Moneda no soportada.")