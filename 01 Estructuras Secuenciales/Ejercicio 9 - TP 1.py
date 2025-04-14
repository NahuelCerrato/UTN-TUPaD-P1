#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

grados_celsius = input("Ingrese grados Celsius: ")
grados_celsius = float(grados_celsius)
grados_fahrenheit = 1.8 * grados_celsius + 32
print(f" en  Fahrenheit equivale a: {grados_fahrenheit}")