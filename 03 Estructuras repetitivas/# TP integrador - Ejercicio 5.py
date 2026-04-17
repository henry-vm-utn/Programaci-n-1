# Ejercicio 5 - "Escape Room: La Arena del Gladiador"

# Paso 1:
# Pedimos el nombre del Gladiador.
nombre_jugador = input("Nombre del Gladiador: ").capitalize()

# Validamos que el nombre tenga solo letras.
while not nombre_jugador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_jugador = input("Nombre del Gladiador: ").capitalize()

# Paso 2:
# Inicializamos las cariables/estadísticas del juego.
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

print("\n--- BIENVENIDO A LA ARENA ---")
print("=== INICIO DEL COMBATE ===")

# Paso 3:
# El combate continúa mientras ambos tengan vida mayor a 0.
while vida_jugador > 0 and vida_enemigo > 0:

    # Mientras sea el turno del Gladiador, mostramos el menú.
    while turno_gladiador:
        print(f"\n{nombre_jugador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        # Validamos que la opción:
        # 1) sea numérica
        # 2) esté entre 1 y 3
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        # Opción 1:
        # Ataque Pesado.
        if opcion == "1":
            # Si la vida del enemigo es menor a 20,
            # el golpe es crítico y multiplica por 1.5.
            if vida_enemigo < 20:
                daño_final = ataque_pesado * 1.5
                vida_enemigo -= daño_final
                print(f"¡Golpe crítico! Atacaste al enemigo por {daño_final} puntos de daño.")
            else:
                daño_final = ataque_pesado
                vida_enemigo -= daño_final
                print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")

            turno_gladiador = False

        # Opción 2:
        # Ráfaga Veloz usando un for de 3 golpes.
        elif opcion == "2":
            print(">> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

            turno_gladiador = False

        # Opción 3:
        # Curar.
        elif opcion == "3":
            # Si quedan pociones, se cura 30 y gasta 1.
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print(">> Te has curado por 30 puntos de vida.")
            else:
                # Si no quedan pociones, pierde el turno igual.
                print("¡No quedan pociones!")

            turno_gladiador = False

    # Turno del enemigo:
    # Solo ataca si sigue vivo.
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo
        print(f">> ¡El enemigo contraataca por {ataque_enemigo} puntos!")

    # Terminando el turno enemigo, vuelve a ser turno del Gladiador.
    turno_gladiador = True

    # Si ambos siguen vivos, avisamos que comienza un nuevo turno.
    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

# Paso 4:
# Fin del juego.
if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre_jugador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")