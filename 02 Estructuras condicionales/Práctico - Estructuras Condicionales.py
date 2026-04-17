# Actividad N° 1 - Mayoría de edad
edad_minima = 18
edad = int(input("Ingrese su edad:"))

# Se añade condición según su edad. Se añade un "else" extra para imprimir si no es menor de edad.

if edad >= edad_minima:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")

# Actividad N° 2 - Nota de usuario

nota_aprobado = 6
nota = float(input("Ingrese nota: "))
#Se añade condición de aprobación.
if nota >= nota_aprobado:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio N° 3 - Sólo números pares

numero = float(input("Ingrese un número PAR: "))
division = numero % 2

#Al usar el operador módulo (%) por 2, sabremos el resto de la divisón, si es 1 (impar) o 0 (par).

if division == 0:
    print("Ha ingresado un número par.")

else:
    print("Por favor, ingrese un número par.")

# Ejercicio N° 4 - Categorías de edad

edad = int(input("Ingrese su edad y le indicaremos categoría: "))

#Con sólo una variable defino las condiciones ayudándome con el operador lógico AND y operadores de comparación.

if edad < 12:
    print("Niño/a.")

elif edad >= 12 and edad < 18:
    print("Adolescente.")

elif edad >= 18 and edad < 30:
    print("Adulto/a joven.")

else:
    print("Adulto/a.")

# Ejercicio N° 5 - Contraseñas

contraseña = input("Ingrese contraseña entre 8 y 14 caracteres: ")

#La función len devuelve el número de ítems en un container. 
caracteres = len(contraseña)

if caracteres >= 8 and caracteres <= 14:
    print("Ha ingresado una contraseña correcta.")

else: 
    print("Por favor, ingrese una contraseña entre 8 y 14 caracteres.")

# Ejercicio N° 6 - Energía en kWh

energia = int(input("Ingrese consumo de energía mensual en kWh: "))

#Defino condiciones con operadores de comparación.
if energia < 150:
    print("Consumo bajo.")

elif energia >= 150 and energia <= 300:
    print("Consumo medio.")

else:
    print("Consumo alto.")

# Ejercicio N° 7 - Frase

texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiouáéíóú":
    print(texto + "!")
else:
    print(texto)

# Ejercicio N° 8 - Nombre 123

nombre = input("Ingrese nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para la primera letra mayúscula): "))

#Se investigan nuevas funciones UPPER, LOWER, TITLE. 
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# Ejercicio N° 9 - Magnitud de terremoto

magnitud = float(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve.")

elif magnitud >= 3 and magnitud < 4:
    print("Leve.")

elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")

elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")

elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
else:
    print("Extremo.")

# Ejercicio N° 10 - Estación del año según fecha y hemisferio.

hemisferio = input("Indique en que hemisferio se encuentra (N ó S): ").upper()
#Definimos de manera numérica meses y días.
mes = int(input("Indique mes del año (1-12): "))
dia = int(input("Indique el día (1-31): "))

#Definimos condiciones necesarias si se está en el polonorte.

if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
    polonorte = "En la fecha y polo indicados, será invierno."
elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
    polonorte = "En la fecha y polo indicados, será primavera."
elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
    polonorte = "En la fecha y polo indicados, será verano."
else:
    polonorte = "En la fecha y polo indicados, será otoño."

if hemisferio == "N":
    print(f"Usted se encuentra en {polonorte}")
else:

# El polo sur, será lo opuesto al norte y se ahorra código simplemente "negándolo".

    if polonorte == "Invierno":
        print("Usted se encuentra en Verano")
    elif polonorte == "Primavera":
        print("Usted se encuentra en Otoño")
    elif polonorte == "Verano":
        print("Usted se encuentra en Invierno")
    else:
        print("Usted se encuentra en Primavera")