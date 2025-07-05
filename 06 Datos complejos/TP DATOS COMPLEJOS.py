#TP-INTEGRADOR
#CERRATO SERGIO NAHUEL


#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado (Ejercicio 1):")
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario actualizado (Ejercicio 2):")
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

# Solo los nombres de las frutas (las claves del diccionario)
lista_frutas = list(precios_frutas.keys())

print("\nLista de frutas (Ejercicio 3):")
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.


agenda = {}


for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero


busqueda = input("\nIngresá el nombre que querés buscar en la agenda: ")

if busqueda in agenda:
    print(f"El número de {busqueda} es: {agenda[busqueda]}")
else:
    print(f"{busqueda} no está en la agenda.")
    
    
#5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.


frase = input("Ingresá una frase: ")


palabras = frase.split()


palabras_unicas = set(palabras)


frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1


print("\nPalabras únicas:")
print(palabras_unicas)

print("\nFrecuencia de cada palabra:")
for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")
    
#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

# Diccionario para almacenar las notas
notas_alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    
    notas_alumnos[nombre] = (nota1, nota2, nota3)


print("\nPromedios:")
for nombre, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
    
    #7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial1 = {"Ana", "Juan", "Pedro", "Lucía"}
parcial2 = {"Pedro", "Lucía", "María", "Sofía"}


ambos = parcial1 & parcial2


solo_uno = parcial1 ^ parcial2


al_menos_uno = parcial1 | parcial2


print("Aprobados en ambos parciales:")
print(ambos)

print("\n🔹 Aprobados solo en uno de los dos:")
print(solo_uno)

print("\n📋 Lista total de aprobados (sin repetir):")
print(al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.


stock = {
    "tornillos": 100,
    "tuercas": 200,
    "clavos": 150
}


print("Stock actual:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad}")


producto = input("\nIngresá el nombre del producto a consultar o modificar: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"{producto} no existe en el stock.")
    respuesta = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if respuesta == 's':
        nuevo_stock = int(input(f"Ingresá la cantidad inicial para {producto}: "))
        stock[producto] = nuevo_stock
        print(f"{producto} fue agregado con {nuevo_stock} unidades.")
    else:
        print("No se realizó ningún cambio.")


print("\nStock actualizado:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad}")
    
    
#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.


agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación",
    ("miércoles", "09:30"): "Consulta médica"
}


print("Agenda actual:")
for clave, evento in agenda.items():
    print(f"{clave}: {evento}")


dia = input("\nIngresá el día a consultar: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada para {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay actividad programada para {dia} a las {hora}.")
    
    
#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores


paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}


capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais


print("Diccionario original (país -> capital):")
print(paises_capitales)

print("\nDiccionario invertido (capital -> país):")
print(capitales_paises)
