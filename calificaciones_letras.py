calificacion = float(input("Introduce la calificación (0-100): "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion < 90:
    letra = "B"
elif 70 <= calificacion < 80:
    letra = "C"
elif 60 <= calificacion < 70:
    letra = "D"
elif 0 <= calificacion < 60:
    letra = "F"
else:
    letra = "Invalida"

match letra:
    case "A": print("Excelente desempeño: A")
    case "B": print("Buen desempeño: B")
    case "C": print("Desempeño regular: C")
    case "D": print("Desempeño suficiente: D")
    case "F": print("Reprobado: F")
    case _: print("Error: Calificación fuera de rango.")