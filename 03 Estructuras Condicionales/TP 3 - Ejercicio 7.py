#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
frase = str(input("Ingrese una frase: "))

if frase.endswith(("a","A","e","E","i","I","o","O","u","U")):
    print(f"{frase}!")
else:
    print(frase)