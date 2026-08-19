# 1. Solicitar la temperatura en Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# 2. Mostrar las opciones y capturar la selección del usuario
print("¿A qué unidad deseas convertir?")
opcion = input("F - Fahrenheit\nK - Kelvin\nSelecciona una opción (F/K): ").strip().upper()

# 3. Evaluar la opción seleccionada
match opcion:
    case "F":
        f = (celsius * 9/5) + 32
        print(f"{celsius}°C equivalen a {f:.2f}°F")
    case "K":
        k = celsius + 273.15
        print(f"{celsius}°C equivalen a {k:.2f}°K")
    case _:
        print("Opción no válida.")