#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
numero_limite = 100
acumulador = 0

for c in range(0, numero_limite):
    numero = int(input("Ingrese numero: "))
    acumulador += numero

print(f"La media de los numeros ingresados es = {acumulador / numero_limite}")