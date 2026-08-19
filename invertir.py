numeros_input = input("Introduce elementos separados por espacios: ")
lista_elementos = numeros_input.split()

lista_invertida = lista_elementos[::-1]

print("Lista original:", lista_elementos)
print("Lista invertida:", lista_invertida)
