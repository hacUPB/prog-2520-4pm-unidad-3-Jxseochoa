def suma(a, b):
	resultado = a + b
	return resultado


# Crear una función que imprima la tabla de cualquier número - bucle for 
def tabla(num):
	for i in range (1,11): 
		producto= i * num
		print(f"{num} x {i} = {producto}")
    #Esta función no tiene ningún retorno


#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

num = int(input("Ingrese un valor: "))
tabla(num)