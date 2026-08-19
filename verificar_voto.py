edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad. ¡Puedes votar!")
else:
    print(f"Te faltan {18 - edad} años para poder votar.")