# Ejercicio 4 - "Escape Room: La Bóveda"

# Variables iniciales del juego.
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cont = 0
bloqueo = False
opcion = ""

# Pedimos el nombre del agente.
agente = input("Ingrese el nombre del agente: ").capitalize()

# Validamos que el nombre tenga solo letras.
while not agente.isalpha():
    agente = input("Error: ingrese un nombre válido (solo letras): ").capitalize()

print(f"Agente: {agente}")

# El juego continúa mientras:
# - haya energía
# - haya tiempo
# - no se hayan abierto las 3 cerraduras
# - y no haya bloqueo por alarma
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:

    # Mostramos el estado actual antes de cada turno.
    print("\n----- ESTADO ACTUAL -----")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    # Menú de acciones.
    opcion = input(
        "\n1. Forzar cerradura"
        "\n2. Hackear panel"
        "\n3. Descansar"
        "\nOpción elegida: "
    )

    # Validamos que la opción sea numérica.
    while not opcion.isdigit():
        opcion = input(
            "Error: ingrese una opción válida.\n"
            "1. Forzar cerradura\n"
            "2. Hackear panel\n"
            "3. Descansar\n"
            "Opción elegida: "
        )

    match opcion:

        # Opción 1:
        # Forzar cerradura.
        case "1":
            forzar_cont += 1
            energia -= 20
            tiempo -= 2

            # Regla anti-spam:
            # Si es la tercera vez seguida forzando, se activa la alarma,
            # se cobra el costo normal y NO se abre cerradura.
            if forzar_cont == 3:
                alarma = True
                print("La cerradura se trabó. Se activó la alarma y no se abrió ninguna cerradura.")

            else:
                # Si la energía está por debajo de 40, hay riesgo de alarma.
                if energia < 40:
                    num_riesgo = input("Riesgo de alarma: elija un número del 1 al 3: ")

                    # Validamos que sea número y que esté entre 1 y 3.
                    while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                        num_riesgo = input("Error: ingrese un número válido del 1 al 3: ")

                    if num_riesgo == "3":
                        alarma = True
                        print("Se activó la alarma.")

                # Si no se activó la alarma, se abre una cerradura.
                if not alarma:
                    cerraduras_abiertas += 1
                    print(f"Has abierto una cerradura. Total abiertas: {cerraduras_abiertas}/3")
                else:
                    print("No se pudo abrir la cerradura por la alarma.")

        # Opción 2:
        # Hackear panel.
        case "2":
            forzar_cont = 0
            energia -= 10
            tiempo -= 3

            print("Iniciando hackeo...")

            # Debe usar un for de 4 pasos mostrando progreso.
            for paso in range(1, 5):
                codigo_parcial += "A"
                print(f"Paso {paso}/4 - Código parcial: {codigo_parcial}")

            # Si el código ya tiene 8 o más caracteres,
            # se abre automáticamente una cerradura si todavía faltan.
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print(f"El panel fue hackeado. Se abrió una cerradura. Total abiertas: {cerraduras_abiertas}/3")

        # Opción 3:
        # Descansar.
        case "3":
            forzar_cont = 0
            energia += 15
            tiempo -= 1

            # La energía no puede superar 100.
            if energia > 100:
                energia = 100

            # Si la alarma está activada, descansar cuesta 10 de energía extra.
            if alarma:
                energia -= 10
                print("La alarma sigue activa. Descansar consumió 10 de energía extra.")

            print(f"Energía luego de descansar: {energia}")
            print(f"Tiempo luego de descansar: {tiempo}")

        # Si el número ingresado no está entre 1 y 3.
        case _:
            print("Error: ingresó una opción fuera de rango.")

    # Regla de bloqueo por alarma:
    # Si la alarma está activa, queda poco tiempo
    # y todavía no se abrió la bóveda, el sistema se bloquea.
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueo = True


# Condiciones de fin del juego.
if cerraduras_abiertas == 3:
    print("\nVICTORIA")
elif bloqueo:
    print("\nDERROTA (BLOQUEO)")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA")