numero = int(input("Ingrese un numero: "))
acumulador = 0
for c in range(0, numero):
    acumulador = acumulador + c
print(f"La suma desde 0 hasta {numero} es de {acumulador}")