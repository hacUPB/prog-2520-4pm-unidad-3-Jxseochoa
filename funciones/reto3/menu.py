RHO = 1.225

def menu():
    while True:
        print("===== MENÚ PRINCIPAL =====")
        print("1. Ejercicio 1 - Estabilidad en turbulencia")
        print("2. Ejercicio 2 - Planeo de emergencia sin motores")
        print("3. Ejercicio 3 - Consumo de combustible")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            print("Gracias por usar el simulador aeronáutico. Hasta pronto.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

def ejercicio1():
    aviones = {
        1: {"nombre": "Cessna 172 Skyhawk", "peso": 10000, "area": 16.2, "v": 65, "cl_base": 0.4, "aoa_inicial": 5},
        2: {"nombre": "Airbus A320", "peso": 600000, "area": 122.6, "v": 130, "cl_base": 0.5, "aoa_inicial": 5},
        3: {"nombre": "Boeing 747-8", "peso": 3500000, "area": 554, "v": 250, "cl_base": 0.6, "aoa_inicial": 5}
    }

    def calcular_sustentacion(cl, rho, v, area):
        return 0.5 * rho * v**2 * cl * area

    print("EJERCICIO 1: ESTABILIDAD EN TURBULENCIA")
    print("Seleccione un avión:")
    print("1. Cessna 172 Skyhawk")
    print("2. Airbus A320")
    print("3. Boeing 747-8")

    opcion = int(input("Ingrese opción (1-3): "))

    if opcion in aviones:
        avion = aviones[opcion]
        peso, area, v = avion["peso"], avion["area"], avion["v"]
        cl_base, aoa = avion["cl_base"], avion["aoa_inicial"]
        estado_final = "Exitoso"

        for segundo in range(1, 9):
            print("Segundo", segundo)
            print("Ángulo de ataque actual:", aoa, "°")
            eleccion_aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ")
            if eleccion_aoa == "a":
                aoa += 1
                print("El ángulo de ataque aumentó a:", aoa, "°")
            elif eleccion_aoa == "d":
                aoa -= 1
                print("El ángulo de ataque disminuyó a:", aoa, "°")
            elif eleccion_aoa == "m":
                print("El ángulo de ataque se mantiene en:", aoa, "°")
            else:
                print("Opción inválida → se mantiene el ángulo de ataque.")

            cl_actual = cl_base + 0.1 * (aoa - avion["aoa_inicial"])
            sustentacion = calcular_sustentacion(cl_actual, RHO, v, area)
            print("Velocidad =", round(v, 1), "m/s | Cl =", round(cl_actual, 3), "| Sustentación =", round(sustentacion, 2), "N")

            if sustentacion >= peso:
                print("Estado: Estable")
            elif sustentacion < 0.5 * peso:
                print("Estado: Pérdida - Fin de simulación")
                estado_final = "Perdida"
                break
            elif sustentacion < 0.8 * peso:
                print("Estado: Crítico")

            print("Velocidad actual:", v, "m/s")
            decision_v = input("¿Velocidad: (a)umentar, (d)isminuir o (m)antener? ")
            if decision_v == "a":
                v += 10
                print("Velocidad aumentó a:", v, "m/s")
            elif decision_v == "d":
                v -= 10
                print("Velocidad disminuyó a:", v, "m/s")
            elif decision_v == "m":
                print("Velocidad se mantiene en:", v, "m/s")
            else:
                print("Opción inválida → se mantiene la velocidad.")

        if estado_final == "Exitoso":
            print("El avión logró atravesar la turbulencia con éxito.")
        else:
            print("El avión no logró superar la turbulencia.")
    else:
        print("Opción inválida. Debe seleccionar 1, 2 o 3.")

def ejercicio2():
    aviones = {
        1: {"nombre": "Piper PA-28 Cherokee", "h_inicial": 600, "L_D": 10, "delta_h": 100},
        2: {"nombre": "Embraer E190", "h_inicial": 1200, "L_D": 14, "delta_h": 150},
        3: {"nombre": "Concorde", "h_inicial": 2000, "L_D": 7, "delta_h": 250}
    }

    print("EJERCICIO 2: PLANEO DE EMERGENCIA SIN MOTORES")
    print("Seleccione un avión:")
    print("1. Piper PA-28 Cherokee")
    print("2. Embraer E190")
    print("3. Concorde")

    opcion = int(input("Ingrese opción (1-3): "))

    if opcion not in aviones:
        print("Opción inválida.")
        return

    avion = aviones[opcion]
    h_actual = avion["h_inicial"]
    L_D = avion["L_D"]
    delta_h = avion["delta_h"]
    distancia = 0
    segundo = 0
    estado_final = "Exitoso"

    print("Has seleccionado:", avion["nombre"])
    print("Altura inicial:", h_actual, "m | Relación L/D base:", L_D, ":1 | Pérdida por segundo:", delta_h, "m")

    while h_actual > 0:
        segundo += 1
        print("Segundo", segundo)
        print("Altura actual:", h_actual, "m | Distancia recorrida:", round(distancia, 2), "m")
        print("Relación L/D actual:", L_D, ":1")
        decision = input("¿Ángulo de picado: (a)umentar, (d)isminuir o (m)antener? ")
        if decision == "a":
            L_D -= 2
            print("El ángulo aumentó → L/D disminuye a", L_D, ":1")
        elif decision == "d":
            L_D += 2
            print("El ángulo disminuyó → L/D aumenta a", L_D, ":1")
        elif decision == "m":
            print("El ángulo se mantiene → L/D =", L_D, ":1")
        else:
            print("Opción inválida → se mantiene el valor.")
        if L_D < 5:
            print("Estado: Crítico, el avión perdió eficiencia de planeo.")
            estado_final = "Fracaso"
            break
        delta_x = L_D * delta_h
        h_actual -= delta_h
        if h_actual < 0:
            h_actual = 0
        distancia += delta_x

    print("FIN DE SIMULACIÓN")
    print("Tiempo total:", segundo, "segundos")
    print("Distancia total recorrida:", round(distancia, 2), "m")
    if estado_final == "Exitoso":
        print("El avión logró planear hasta el suelo con éxito.")
    else:
        print("El avión no logró mantener un planeo eficiente y aterrizó de forma crítica.")

def ejercicio3():
    consumo_ascenso = 75
    consumo_crucero = 50
    consumo_descenso = 37.5
    intervalo = 5
    min_seguridad = 1500

    print("EJERCICIO 3: CONSUMO DE COMBUSTIBLE")
    combustible_ini = float(input("Ingrese la cantidad inicial de combustible (litros): "))
    t_ascenso = int(input("Ingrese la duración del ascenso (minutos): "))
    t_crucero = int(input("Ingrese la duración del crucero (minutos): "))
    t_descenso = int(input("Ingrese la duración del descenso (minutos): "))

    combustible_act = combustible_ini
    tiempo_total = 0

    def simular_fase(nombre_fase, tiempo_fase, consumo_fase, combustible_act, tiempo_total):
        for minuto in range(0, tiempo_fase, intervalo):
            delta_combustible = consumo_fase * intervalo
            combustible_act -= delta_combustible
            tiempo_total += intervalo
            if combustible_act <= 0:
                print(f"Minuto {tiempo_total}: Sin combustible durante {nombre_fase}. Vuelo fallido.")
                return 0, tiempo_total, "Vuelo fallido"
            elif combustible_act <= min_seguridad:
                print(f"Minuto {tiempo_total}: Combustible {combustible_act:.2f} L → Emergencia en {nombre_fase}.")
            else:
                print(f"Minuto {tiempo_total}: Combustible {combustible_act:.2f} L → Normal en {nombre_fase}.")
        return combustible_act, tiempo_total, "Continuar"

    combustible_act, tiempo_total, estado = simular_fase("ascenso", t_ascenso, consumo_ascenso, combustible_act, tiempo_total)
    if estado == "Vuelo fallido":
        return
    combustible_act, tiempo_total, estado = simular_fase("crucero", t_crucero, consumo_crucero, combustible_act, tiempo_total)
    if estado == "Vuelo fallido":
        return
    combustible_act, tiempo_total, estado = simular_fase("descenso", t_descenso, consumo_descenso, combustible_act, tiempo_total)
    if estado == "Vuelo fallido":
        return

    print("FIN DEL VUELO")
    print(f"Tiempo total: {tiempo_total} minutos")
    print(f"Combustible final: {combustible_act:.2f} L")
    if combustible_act >= min_seguridad:
        print("Resultado: Vuelo exitoso. Aterrizaje con reserva suficiente.")
    elif combustible_act > 0:
        print("Resultado: Vuelo completado en emergencia. Aterrizaje con menos de la reserva mínima.")
    else:
        print("Resultado: Vuelo fallido. Sin combustible antes de aterrizar.")

menu()


