import random

numero_secreto = random.randint(1, 100)
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
