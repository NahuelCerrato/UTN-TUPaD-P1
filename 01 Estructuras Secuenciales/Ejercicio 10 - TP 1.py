#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero_1 = input("Ingrese el primer numero: " )
numero_2 = input("Ingrese el segundo numero: " )
numero_3 = input("Ingrese el tercer numero: " )

numero_1 = int(numero_1)
numero_2 = int(numero_2)
numero_3 = int(numero_3)

promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los numeros es: {promedio}") 