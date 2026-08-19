parciales = float(input("Calificación de parciales (0-100): "))
proyecto = float(input("Calificación del proyecto (0-100): "))
examen = float(input("Calificación del examen (0-100): "))

nota_final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
print(f"La calificación final es: {nota_final:.2f}")