print ("Por favor ingrese a su nombre.")
nombre = input()
print ("Bienvenido ", nombre)
# Calcular el IMC
# IMC = peso / estatura **2

# Leer estatura
estatura = input ("Ingrese su estatura en metros: ")
estatura = float (estatura)
# Leer peso
peso = input ("Ingrese su peso en kilogramos: ")
peso = float (peso)
#Calcular el IMC
IMC = peso / estatura ** 2
# Mostrar IMC
print ("Su IMC = ", IMC)

# Su IMC dice que:
if IMC < 18.49:
    print("Bajo peso")
else:
    if IMC < 24.99:
        print("Peso normal")
    else:
        if IMC < 29.99:
            print("Sobrepeso")
        else:
            if IMC < 39.99:
                print("Obesidad")
            else:
                if IMC >= 40:
                    print("Obesidad extrema")