# =======================================
# Simulador Aeronáutico Interactivo
# Menú principal + Ejercicio 1 corregido
# =======================================

import random

# Constante global
RHO = 1.225  # densidad del aire (kg/m³)

# ================================
# MENÚ PRINCIPAL
# ================================
def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Estabilidad en turbulencia")
        print("2. Planeo de emergencia sin motores (pendiente)")
        print("3. Control de ascenso y techo de servicio (pendiente)")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            problema_turbulencia()   # Llama al Ejercicio 1
        elif opcion == "2":
            print("\n⚠️ Ejercicio 2 aún no implementado.")
        elif opcion == "3":
            print("\n⚠️ Ejercicio 3 aún no implementado.")
        elif opcion == "4":
            print("Gracias por usar el simulador aeronáutico. ¡Hasta pronto! ✈️")
            break
        else:
            print("⚠️ Opción inválida, intente de nuevo.")

# ================================
# EJERCICIO 1: Estabilidad en turbulencia
# ================================
def problema_turbulencia():
    """
    Simulación de estabilidad en turbulencia.
    El usuario selecciona uno de los tres aviones predefinidos
    y el programa simula 8 segundos de turbulencia,
    calculando la sustentación y el estado del vuelo.
    """

    # --- Aviones predefinidos ---
    aviones = {
        1: {"nombre": "Cessna 172 Skyhawk", "peso": 10000, "area": 16.2, "v": 65, "cl": 0.4},
        2: {"nombre": "Airbus A320", "peso": 600000, "area": 122.6, "v": 130, "cl": 0.5},
        3: {"nombre": "Boeing 747-8", "peso": 3500000, "area": 554, "v": 250, "cl": 0.6}
    }

    # --- Función para calcular sustentación ---
    def calcular_sustentacion(cl, rho, v, area):
        """
        Calcula la sustentación de un avión usando la fórmula:
        L = 0.5 * rho * v^2 * Cl * A
        """
        return 0.5 * rho * v**2 * cl * area

    # Selección de avión
    print("\n--- Estabilidad en turbulencia ---")
    print("Seleccione un avión:")
    print("1. Cessna 172 Skyhawk")
    print("2. Airbus A320")
    print("3. Boeing 747-8")

    opcion = int(input("Ingrese opción (1-3): "))

    if opcion in aviones:
        avion = aviones[opcion]
        peso, area, v, cl = avion["peso"], avion["area"], avion["v"], avion["cl"]
        print(f"\nHas seleccionado: {avion['nombre']}")
        print(f"Peso: {peso} N | Área alar: {area} m² | Velocidad inicial: {v} m/s | Cl base: {cl}")

        for segundo in range(1, 9):
            print(f"\nSegundo {segundo}:")

            aoa = input("¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener? ").strip().lower()
            if aoa == "a":
                cl_actual = cl + 0.05
            elif aoa == "d":
                cl_actual = cl - 0.05
            else:
                cl_actual = cl  # mantener

            sustentacion = calcular_sustentacion(cl_actual, RHO, v, area)

            print(f"Velocidad = {v:.1f} m/s | Cl = {cl_actual:.3f} | Sustentación = {sustentacion:.2f} N")

            if sustentacion >= peso:
                print("Estado: Estable")
            elif sustentacion < 0.5 * peso:
                print("Estado: Pérdida - Fin de simulación")
                break
            elif sustentacion < 0.8 * peso:
                print("Estado: Crítico")

            decision = input("¿Velocidad: (a)umentar o (m)antener? ")
            if decision == "a":
                v += 10
            elif decision == "m":
                pass
            else:
                print("Opción inválida → se mantiene la velocidad.")

        else:
            print(" El avión logró atravesar la turbulencia con éxito.")
    else:
        print("Opción inválida. Debe seleccionar 1, 2 o 3.")

menu()
