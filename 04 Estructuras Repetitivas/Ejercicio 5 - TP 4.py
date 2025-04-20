import random
numero = random.randint(1,9)
numero_adivina = int(input("Ingrese numero a adivinar: "))
intentos = 0
while numero != numero_adivina:
    intentos = intentos + 1
    numero_adivina = int(input("Incorrecto, numero a adivinar: "))

print(f"Correcto, era {numero} y lo adivinaste en {intentos} intentos")
