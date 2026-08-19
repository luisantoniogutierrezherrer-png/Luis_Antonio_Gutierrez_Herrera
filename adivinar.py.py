import time

# Generamos un numero entre 1 y 100 usando los milisegundos del reloj actual
numero_secreto = int((time.time() * 1000) % 100) + 1

print("He pensado un numero entre 1 y 100. ¡Adivinalo!")

while True:
    intento = int(input("Introduce tu numero: "))
    if intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("¡Felicidades! Adivinaste el numero.")
        break
