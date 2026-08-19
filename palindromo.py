texto = input("Introduce una palabra o frase: ")

texto_limpio = ""
for caracter in texto.lower():
    if caracter.isalnum():
        texto_limpio += caracter

texto_invertido = texto_limpio[::-1]

if texto_limpio == texto_invertido:
    print("Es un palindromo.")
else:
    print("No es un palindromo.")
