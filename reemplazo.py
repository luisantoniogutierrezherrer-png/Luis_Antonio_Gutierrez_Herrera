texto = input("Introduce una frase o palabra: ")
buscar = input("Introduce el caracter que deseas cambiar: ")
reemplazo = input("Introduce el nuevo caracter: ")

texto_modificado = texto.replace(buscar, reemplazo)

print(f"Resultado final: {texto_modificado}")
