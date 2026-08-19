mes = input("Introduce el nombre del mes: ").strip().lower()
match mes:
    case "marzo" | "abril" | "mayo":
        print("La estación es: Primavera")
    case "junio" | "julio" | "agosto":
        print("La estación es: Verano")
    case "septiembre" | "octubre" | "noviembre":
        print("La estación es: Otoño")
    case "diciembre" | "enero" | "febrero":
        print("La estación es: Invierno")
    case _:
        print("Mes no válido. Revisa la ortografía.")