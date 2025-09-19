'''
Función: Menú
Paramétros de entrada: ninguno
Ejecución: imprimir en pantalla 4 opciones diferentes. Solicitar que se elija una opción y la guarde en una variable
Valor de retorno: Opción elegida
'''
def menu():
    print("Opción")
    print("1. Encabezado")
    print("2. Porcentaje ")
    print("3. Mensaje")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def encabezado(mensaje):
    print("Nombre: Jose Ochoa")
    print("ID: 000567707")
    print(mensaje)

def porcentaje(valor1, valor2):
    pass


eleccion = menu()
match(eleccion):
    case 1:
        mensaje= input("Ingresa una frase: ")
        #Imprimir información de mí. 
        # Parametro: Mensaje que se imprime dentro de la función
    case 2:
        pass
        #Parámetro 1: Valor total
        #Parámetro 2: Porcentaje
        #Retorno: Valor del procentaje

    case 3:
        pass 
        #No recibe ningún parámetro y no devuelve un resultado
        #Imprime en pantalla un mensaje de cierre de programa