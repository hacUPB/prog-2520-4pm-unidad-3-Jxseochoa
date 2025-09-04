# Determinar si un numero es par o impar
# Leer numero
numero = int(input("Ingrese un numero entero: "))
residuo = numero % 2
# Si residuo es cero, es par
if residuo == 0:
    print(numero, "es par.")
else:
    print(numero, "es impar.")