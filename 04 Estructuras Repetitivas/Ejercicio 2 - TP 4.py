#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num = int(input("Ingrese numero: "))
num_1 = num
num_digitos = 0

while num != 0:
    num = num // 10
    num_digitos += 1

print(f"La cantidad de dígitos que contiene {num_1} es de {num_digitos}")