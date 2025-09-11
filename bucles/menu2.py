'''
# Utilizamos una variables tipo booleana -> una bandera 
control = True 

while control == True:
    print("1. Entradas\n2, Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir)")
opcion= int(input("Elija una opción: "))

    match opcion: 
        case 1: 
            print("1. Patacón con hogao")
            print("2. Yuca con chicharrón.")
            print("3. Guineo con suero")
        case 2:
            print("1. Solomito")
            print("2. Hamburguesa.")
            print("3. Sushi")
        case 3:
            print("1. Limonada")
            print("2. Jugos naturales")
            print("3. Cerveza")
        case 4:
            print("1. Tres leches")
            print("2. Tiramisú")
            print("3. Rollos de canela")
        case 5:
            control = False
        case _:
            print("Opción no válida")

'''