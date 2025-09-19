import ejerciciosreto3

def menu():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Ejercicio 1: Estabilidad en turbulencia")
        print("2. Ejercicio 2: Planeo de emergencia sin motores")
        print("3. Ejercicio 3: Consumo de combustible")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            ejerciciosreto3.ejercicio1()
        elif opcion == "2":
            ejerciciosreto3.ejercicio2()
        elif opcion == "3":
            ejerciciosreto3.ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()


