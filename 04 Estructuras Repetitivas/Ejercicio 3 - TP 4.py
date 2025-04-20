num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
acumulador = 0


for c in range(num_1+1,num_2):
    acumulador = acumulador + c
    
print(f"La suma de todos los numeros comprendidos entre esos dos valores es de: {acumulador}")