#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

#Forma 1:
lista_anidada_1 = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada_1)

#Forma 2:
lista_anidada_2 = []

lista_anidada_2.append(15)
lista_anidada_2.append(True)
lista_anidada_2.append([])
lista_anidada_2[2].append(25.5)
lista_anidada_2[2].append(57.9)
lista_anidada_2[2].append(30.6)
lista_anidada_2.append(False)

print(lista_anidada_2)