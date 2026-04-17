# Ejercicio 2 - "Acceso al campus y menú."

# Requisito 1
usuario_correcto = "alumno"
clave_correcta = "python123"

for intentos in range(1, 4):
    usuario_ingresado = input(f"Intento {intentos}/3 - Usuario: ")
    clave_ingresada = input("Clave: ")

    # Si el usuario y/o clave son incorrectos
    if usuario_ingresado != usuario_correcto or clave_ingresada != clave_correcta:
        print("Error: credenciales inválidas.")

        # Si llega al tercer intento y sigue mal, bloquea la cuenta
        if intentos == 3:
            print("Cuenta bloqueada.")

    # Si el usuario y la clave son correctos, ingresamos al menú
    elif usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")

        accion = ""

        while accion != "4":
            print("\n1) Estado    \n2) Cambiar clave    \n3) Mensaje    \n4) Salir")
            accion = input("Seleccione una opción del 1 al 4: ")

            # Validación: debe ser número
            if not accion.isdigit():
                print("Error: ingrese un número válido.")

            # Si es número, vemos qué opción eligió!
            else:
                if accion == "1":
                    print("Estado: Inscripto")

                elif accion == "2":
                    clave_nueva = input("Nueva clave: ")

                    if len(clave_nueva) < 6:
                        print("Error: mínimo 6 caracteres.")
                    else:
                        clave_nueva_confirmar = input("Ingrese nuevamente la contraseña: ")

                        if clave_nueva == clave_nueva_confirmar:
                            clave_correcta = clave_nueva
                            print("La contraseña se ha actualizado")
                        else:
                            print("Las contraseñas no coinciden.")

                elif accion == "3":
                    print("¡Non mollare!")

                elif accion == "4":
                    print("Ha cerrado sesión.")

                else:
                    print("Error: opción fuera de rango.")

        break