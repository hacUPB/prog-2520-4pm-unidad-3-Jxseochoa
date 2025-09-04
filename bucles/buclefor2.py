numero = int(input("Ingrese el número entero positivo:"))
for i in range(1, numero + 1):
    for j in range(1, i+1):
        print(j,end=' ')
    print()