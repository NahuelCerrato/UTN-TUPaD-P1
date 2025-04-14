#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

radio = input("Ingrese radio: ")
radio = float(radio)
area = 3.141592653589793 * radio * radio
perimetro = 2 * 3.141592653589793 * radio

print(f"El área del círculo es: {area} y su perimetro es: {perimetro}")