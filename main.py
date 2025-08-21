def diagnostico_auto():
    print("Bienvenido al sistema de diagnóstico de autos.")

    arranca = input("¿El auto arranca? (sí/no): ").strip().lower()

    if arranca == "no":
        luces = input("¿Las luces del tablero están encendidas? (sí/no): ").strip().lower()
        if luces == "no":
            print("Posible causa: batería descargada")
        else:
            print("Posible causa: fallo en el motor de arranque")

    else:
        se_apaga = input("¿El auto se apaga al acelerar? (sí/no): ").strip().lower()
        if se_apaga == "s":
            print("Posible causa: problema en el suministro de combustible")
        else:
            humo = input("¿El auto tiene humo por el escape? (sí/no): ").strip().lower()
            if humo == "s":
                color_humo = input("¿De qué color es el humo? (negro/blanco): ").strip().lower()
                if color_humo == "negro":
                    print("Posible causa: mezcla rica de combustible")
                elif color_humo == "blanco":
                    print("Posible causa: falla en la junta de culata")
                else:
                    print("No se pudo determinar la causa por el color del humo")
            else:
                print("No se detectó ninguna falla evidente")



diagnostico_auto()
