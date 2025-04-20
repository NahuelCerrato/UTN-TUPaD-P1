#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = int(input("Ingrese un número entero positivo: "))

invertido = 0

while num > 0:
    digit = num % 10
    invertido = (invertido * 10) + digit
    num = num // 10  # truncar la división entera

print("El número invertido es:", invertido)