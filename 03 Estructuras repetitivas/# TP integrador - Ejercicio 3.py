# Ejercicio 3 - "Agenda de Turnos con Nombres (sin listas)"

# Requisito 1:
# Definir los espacios de turnos vacíos para cada día.
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Contadores de turnos ocupados por día.
cont_lunes = 0
cont_martes = 0

# Variable para controlar el menú.
opcion = ""

# Requisito 1:
# Pedir nombre del operador (solo letras).
operador = input("Ingrese el nombre del operador: ").capitalize()

while not operador.isalpha():
    operador = input("Error: ingrese un nombre válido (solo letras): ").capitalize()

print(f"Operador: {operador}")

# Requisito 2:
# Mostrar menú repetitivo hasta elegir la opción 5.
while opcion != "5":
    print("\n1) Reservar turno    \n2) Cancelar turno    \n3) Ver agenda del día    \n4) Ver resumen general    \n5) Cerrar sistema")
    opcion = input("Opción: ")

    # Validación del menú:
    # La opción debe ser numérica.
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
    else:
        match opcion:

            # Opción 1:
            # Reservar un turno en Lunes o Martes.
            case "1":
                dia = input("Elegir día (1=Lunes, 2=Martes): ")

                # Validación del día:
                # Debe ser número y estar entre 1 y 2.
                while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                    dia = input("Error: ingrese un día válido (1=Lunes, 2=Martes): ")

                # Pedimos el nombre del paciente.
                paciente = input("Ingrese el nombre del paciente: ").capitalize()

                # Validamos que el nombre tenga solo letras.
                while not paciente.isalpha():
                    paciente = input("Error: ingrese un nombre válido (solo letras): ").capitalize()

                # Si el día es Lunes:
                # Verificamos que el paciente no esté repetido
                # y lo guardamos en el primer espacio libre.
                if dia == "1":
                    if paciente != lunes1 and paciente != lunes2 and paciente != lunes3 and paciente != lunes4:
                        if lunes1 == "":
                            lunes1 = paciente
                            cont_lunes += 1
                            print("Turno reservado correctamente para Lunes.")
                        elif lunes2 == "":
                            lunes2 = paciente
                            cont_lunes += 1
                            print("Turno reservado correctamente para Lunes.")
                        elif lunes3 == "":
                            lunes3 = paciente
                            cont_lunes += 1
                            print("Turno reservado correctamente para Lunes.")
                        elif lunes4 == "":
                            lunes4 = paciente
                            cont_lunes += 1
                            print("Turno reservado correctamente para Lunes.")
                        else:
                            print("Error: los turnos de Lunes están completos.")
                    else:
                        print("Error: el paciente ya tiene un turno reservado en Lunes.")

                # Si el día es Martes:
                # Verificamos que el paciente no esté repetido
                # y lo guardamos en el primer espacio libre.
                elif dia == "2":
                    if paciente != martes1 and paciente != martes2 and paciente != martes3:
                        if martes1 == "":
                            martes1 = paciente
                            cont_martes += 1
                            print("Turno reservado correctamente para Martes.")
                        elif martes2 == "":
                            martes2 = paciente
                            cont_martes += 1
                            print("Turno reservado correctamente para Martes.")
                        elif martes3 == "":
                            martes3 = paciente
                            cont_martes += 1
                            print("Turno reservado correctamente para Martes.")
                        else:
                            print("Error: los turnos de Martes están completos.")
                    else:
                        print("Error: el paciente ya tiene un turno reservado en Martes.")

            # Opción 2:
            # Cancelar un turno por nombre.
            case "2":
                dia = input("Ingrese el día del turno a cancelar (1=Lunes, 2=Martes): ")

                # Validamos que el día sea correcto.
                while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                    dia = input("Error: ingrese un día válido (1=Lunes, 2=Martes): ")

                paciente = input("Ingrese el nombre del paciente: ").capitalize()

                # Validamos el nombre del paciente.
                while not paciente.isalpha():
                    paciente = input("Error: ingrese un nombre válido (solo letras): ").capitalize()

                # Buscamos el paciente en el día elegido.
                # Si existe, cancelamos el turno y dejamos el espacio vacío.
                if dia == "1":
                    if lunes1 == paciente:
                        lunes1 = ""
                        cont_lunes -= 1
                        print("Turno cancelado correctamente en Lunes.")
                    elif lunes2 == paciente:
                        lunes2 = ""
                        cont_lunes -= 1
                        print("Turno cancelado correctamente en Lunes.")
                    elif lunes3 == paciente:
                        lunes3 = ""
                        cont_lunes -= 1
                        print("Turno cancelado correctamente en Lunes.")
                    elif lunes4 == paciente:
                        lunes4 = ""
                        cont_lunes -= 1
                        print("Turno cancelado correctamente en Lunes.")
                    else:
                        print("Error: el paciente no tiene turno reservado en Lunes.")

                elif dia == "2":
                    if martes1 == paciente:
                        martes1 = ""
                        cont_martes -= 1
                        print("Turno cancelado correctamente en Martes.")
                    elif martes2 == paciente:
                        martes2 = ""
                        cont_martes -= 1
                        print("Turno cancelado correctamente en Martes.")
                    elif martes3 == paciente:
                        martes3 = ""
                        cont_martes -= 1
                        print("Turno cancelado correctamente en Martes.")
                    else:
                        print("Error: el paciente no tiene turno reservado en Martes.")

            # Opción 3:
            # Ver la agenda completa de un día.
            case "3":
                dia = input("Ingrese un día para ver la agenda (1=Lunes, 2=Martes): ")

                # Validamos que el día sea correcto.
                while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                    dia = input("Error: ingrese un día válido (1=Lunes, 2=Martes): ")

                # Mostramos los turnos en orden.
                # Si un turno está vacío, mostramos "(libre)".
                if dia == "1":
                    print("\nAgenda de Lunes")

                    if lunes1 == "":
                        print("Turno 1: (libre)")
                    else:
                        print(f"Turno 1: {lunes1}")

                    if lunes2 == "":
                        print("Turno 2: (libre)")
                    else:
                        print(f"Turno 2: {lunes2}")

                    if lunes3 == "":
                        print("Turno 3: (libre)")
                    else:
                        print(f"Turno 3: {lunes3}")

                    if lunes4 == "":
                        print("Turno 4: (libre)")
                    else:
                        print(f"Turno 4: {lunes4}")

                elif dia == "2":
                    print("\nAgenda de Martes")

                    if martes1 == "":
                        print("Turno 1: (libre)")
                    else:
                        print(f"Turno 1: {martes1}")

                    if martes2 == "":
                        print("Turno 2: (libre)")
                    else:
                        print(f"Turno 2: {martes2}")

                    if martes3 == "":
                        print("Turno 3: (libre)")
                    else:
                        print(f"Turno 3: {martes3}")

            # Opción 4:
            # Ver el resumen general del sistema.
            case "4":
                disponibles_lunes = 4 - cont_lunes
                disponibles_martes = 3 - cont_martes

                print("\nResumen general")
                print(f"Lunes - Ocupados: {cont_lunes} | Disponibles: {disponibles_lunes}")
                print(f"Martes - Ocupados: {cont_martes} | Disponibles: {disponibles_martes}")

                # Informamos qué día tiene más turnos ocupados
                # o si hay empate.
                if cont_lunes > cont_martes:
                    print("Día con más turnos ocupados: Lunes")
                elif cont_martes > cont_lunes:
                    print("Día con más turnos ocupados: Martes")
                else:
                    print("Hay empate entre Lunes y Martes.")

            # Opción 5:
            # Cerrar el sistema.
            case "5":
                print("El sistema ha finalizado.")

            # Si el número ingresado no está entre 1 y 5.
            case _:
                print("Error: opción fuera de rango.")