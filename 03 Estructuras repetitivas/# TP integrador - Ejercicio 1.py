# TP integrador
# Ejercicio 1 - "Caja de Kiosko"

nombre_cliente = input("Ingrese el nombre del cliente: ")
#Requisito 1
#Se valida con while y se verifica si el nombre es igual a un espacio vacío ó contiene algo distinto a una letra (validado con .isalpha())
while nombre_cliente == "" or not nombre_cliente.isalpha():
    nombre_cliente = input("Ingresar nuevamente el nombre, sólo letras son admitidas:")

#Requisito 2
#Usando while se verifica y validad que se ingrese información, sea correcta y sólo numérica.
cant_prod = (input("Ingresar cantidad de productos que desea comprar: "))
while cant_prod == "" or not cant_prod.isdigit() or (int(cant_prod) <= 0):
    cant_prod = (input("Ingrese una número entero y positivo: "))
cant_prod = int(cant_prod)

total_sin_descuento = 0
total_con_descuento = 0

#Requisito 3
#Se ingresará el precio precio del producto, si tiene descuento y en cuyo caso aplicar el mismo. 
for i in range(1,cant_prod + 1):
    precio = (input(f"Ingresar precio del producto número {i} sin decimales: "))
    while precio == "" or not precio.isdigit() or (int(precio) <= 0):
        precio = input("Ingrese un precio válido, sin decimales: ")
#Si tiene descuento S/N en minúsculas o mayúsculas.
    descuento = input("¿Tiene éste producto descuento del 10%? (S/N): ").lower()
    while descuento != "n" and descuento != "s":
        descuento = input("Ingrese una entrada válida (S/N): ").lower()

    precio = int(precio)

#En las siguientes lineas se añaden acumuladores que vamos a necesitar para imprimir la información al final del programa.
    total_sin_descuento += precio
    if descuento == "n":
        print(f"El producto {i} no posee descuento.")
        precio_final = precio
    else:
        precio_final = precio * 0.9

    total_con_descuento += precio_final
    print(f"El precio de este producto será {precio_final:.2f}")

#Calculo ahorro y promedio de precio por producto.
ahorro_total = total_sin_descuento - total_con_descuento
promedio_producto = total_con_descuento / cant_prod

#Se imprimen los datos solicitados.

print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_producto:.2f}")

