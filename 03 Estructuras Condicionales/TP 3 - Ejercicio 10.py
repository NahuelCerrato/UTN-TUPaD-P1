#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("Ingrese hemisferio N/S: ")).lower()
mes = str(input("Ingrese mes: ")).lower()
dia = int(input("Ingrese dia: "))

if hemisferio == "n":
    if mes == "diciembre":
        if dia >= 21 and dia <= 31:
            estacion = "Invierno"
        else: 
            estacion = "Otoño"
    elif mes == "marzo":
        if dia >= 21 and dia <= 31:
            estacion = "Primavera"
        else:
            estacion = "Invierno"
    elif mes == "junio":
        if dia >= 21 and dia <= 31:
            estacion = "Verano"
        else:
            estacion = "Primavera"
    elif mes == "septiembre":
        if dia >= 21 and dia <= 31:
            estacion = "Otoño"
        else:
            estacion = "Verano"
    elif mes == "enero" or mes == "febrero":
        estacion = "Invierno"
    elif mes == "abril" or mes == "mayo":
        estacion = "Primavera"
    elif mes == "julio" or mes == "agosto":
        estacion = "verano"
    elif mes == "octubre" or mes == "noviembre":
        estacion = "Otoño"
else: 
    if hemisferio == "s":
        if mes == "diciembre":
            if dia >= 21 and dia <= 31:
                estacion = "Verano"
            else: 
                estacion = "Primavera"
        elif mes == "marzo":
            if dia >= 21 and dia <= 31:
                estacion = "Otoño"
            else:
                estacion = "Verano"
        elif mes == "junio":
            if dia >= 21 and dia <= 31:
                estacion = "Invierno"
            else:
                estacion = "Otoño"
        elif mes == "septiembre":
            if dia >= 21 and dia <= 31:
                estacion = "Primavera"
            else:
                estacion = "Invierno"
        elif mes == "enero" or mes == "febrero":
            estacion = "Verano"
        elif mes == "abril" or mes == "mayo":
            estacion = "Otoño"
        elif mes == "julio" or mes == "agosto":
            estacion = "Invierno"
        elif mes == "octubre" or mes == "noviembre":
            estacion = "Primavera"

print(f"La fecha ingresada es {dia} de {mes} y su estación es: {estacion}")