print("Introduce caracteres uno por uno. El programa termina si introduces un espacio:")

while True:
    c = input("Introduce un caracter: ")
    if c == " ":
        print("Programa finalizado por espacio detectado.")
        break
    if len(c) != 1:
        print("Por favor, introduce solo un caracter.")
        continue
    if c.isalpha():
        letra = c.lower()
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            print(f"'{c}' es una Vocal.")
        else:
            print(f"'{c}' es una Consonante.")
    else:
        print(f"'{c}' no es una letra alfabetica.")
