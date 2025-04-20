#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
numero = int(input("Ingrese numero: "))
acumulador = 0

while numero != 0:
    acumulador = acumulador + numero
    numero = int(input("Ingrese numero o ingrese 0 para completar la suma: "))

print(f"El total es: {acumulador}")