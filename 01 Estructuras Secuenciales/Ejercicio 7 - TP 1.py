#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos


numero_1 = input("Ingrese el primer numero: " )
numero_2 = input("Ingrese el segundo numero: ")

numero_1 = int(numero_1)
numero_2 = int(numero_2)

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
if numero_2 != 0:
        division = numero_1 / numero_2
        print(f"El resultado de la division es:{division} ")
else: print("Error, no se puede dividir por 0")
print(f"El resultado de la suma es : {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")