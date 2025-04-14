#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

altura = input("Ingrese altura: ")
altura = float(altura)
peso = input("Peso: ")
peso = float(peso)
if altura > 0: 
    imc = ( peso / (altura * altura) )
    print(f"Su IMC es de:{imc} ")
else: print(f"Error, su altura ingresada es: {altura} y no se puede dividir por: {altura}")