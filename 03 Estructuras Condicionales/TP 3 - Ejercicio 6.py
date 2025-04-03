from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50) if i]

media = mean(numeros_aleatorios)
moda = mode(numeros_aleatorios)
mediana = median (numeros_aleatorios)
print(f"La media es: {media}")
print(f"La mediana es: {mediana}")
print(f"La moda es: {moda}")

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
else: 
    if media == mediana and mediana == moda:
        print("Sin sesgo")
