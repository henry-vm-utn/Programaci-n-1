# Actividad 1 - Hola mundo

print(f"Hola mundo")

#Actividad 2 - Saludo

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
print(f"{nombre} {apellido}")

#Actividad 3 - Información

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = int(input("Escriba su edad: "))
residencia = input("Ingrese residencia actual: ")

print(f"Hola {nombre} {apellido}, de {edad} años de edad y residente en {residencia}.")

#Actividad 4 - Perímetro
radio = float(input("Ingrese radio del círculo en cm para obtener área y perímetro: "))
import math
from math import pi
perímetro = float(radio * pi)
area = float((pi * radio**2)/2)

print(f"El perímetro sería del círculo de radio {radio}cm es {perímetro}cm y el area es {area}cm2.")

#Actividad 5 - Cantidad de segundos  en horas

segundos = int(input("Ingrese cantidad de segundos a transformar a horas: "))
horas = float(segundos / 3600)

print(f"Esos segundos equivalen a {horas} horas.")

#Actividad 6 

num = int(input("Escriba un número para obtener la tabla de multiplicar del mismo: "))

num0 = (num * 0)
num1 = (num * 1)
num2 = (num * 2)
num3 = (num * 3)
num4 = (num * 4)
num5 = (num * 5)
num6 = (num * 6)
num7 = (num * 7)
num8 = (num * 8)
num9 = (num * 9)


print(f"Por 0 = {num0}")
print(f"Por 1 = {num1}")
print(f"Por 2 = {num2}")
print(f"Por 3 = {num3}")
print(f"Por 4 = {num4}")
print(f"Por 5 = {num5}")
print(f"Por 6 = {num6}")
print(f"Por 7 = {num7}")
print(f"Por 8 = {num8}")
print(f"Por 9 = {num9}")

#Actividad 7 - Operaciones básicas con dos números

numero1 = int(input("Ingrese el primer número entero distinto de cero:"))
numero2 = int(input("Ingrese el segundo número entero distinto de cero:"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Division: {numero1} / {numero2} = {division}")
print(f"Multiplicación: {numero1} x {numero2} = {multiplicacion}")

#Actividad 8 - Índice de masa corporal (IMC)

print(f"Calcularé su índice de masa corporal, favor de ingresar los datos solicitados:")

altura = float(input("Ingrese su altura:"))
peso = float(input("Ingrese su peso en kilogramos:"))
IMC = peso / altura ** 2

print(f"Su IMC es {IMC:.2f}")

#Actividad 9 - Celsius a Fahrenheit

celsius = float(input("Ingrese temperatura en grados Celsius para obtener su equivalenciia a Fahrenheit:"))

fahrenheit = (9/5) * celsius + 32

print(f"La equivalencia es igual a {fahrenheit:.2f}°F")

#Actividad 10 - Promedio

n1 = float(input("Ingrese primer número a promediar entre 3:"))
n2 = float(input("Ingrese segundo número a promediar entre 3:"))
n3 = float(input("Ingrese tercer número a promediar entre 3:"))

Promedio = (n1 + n2 + n3) / 3

print(f"El promedio entre los 3 números brindados será: {Promedio:.2f}")
