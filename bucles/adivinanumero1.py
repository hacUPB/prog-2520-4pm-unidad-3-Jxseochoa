#import random
from random import randint

'''
Variable de entrada
Nombre          Tipo
numero          int

Variable de salida
intentos        int     contador

Variable de control
numero          int
'''

#num_aleatorio = random.randint(0,50)
num_aleatorio = randint(1,100)
intentos = 0
numero = -1
#numero = -1
flag = True
#while numero != num_aleatorio:
while flag == True:
    while True:
     numero != num_aleatorio
     numero = int(input("Adivina el número oculto entre 1 y 100: 98"))
    intentos += 1
    if numero > num_aleatorio:
        print("EL numero oculto es menor")
    elif numero < num_aleatorio:
        print("El numero oculto es mayor")
    else:
        print("Felicidades, adivinaste...")
        flag = False
        break


print(f"Adivinaste en {intentos} intentos")
