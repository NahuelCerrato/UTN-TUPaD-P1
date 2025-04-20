#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numero_limite = 5
contador_pares = 0
contador_positivos = 0
contador_impares = 0
contador_negativos = 0

for c in range(0, numero_limite):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        contador_pares +=1
    else:
        contador_impares +=1
    if numero > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1
print(f"Los numeros pares son: {contador_pares}")
print(f"Los numeros impares son: {contador_impares}")
print(f"Los numeros positivos son: {contador_positivos}")
print(f"Los numeros negativos son: {contador_negativos}")