numero=0
suma=0
media=0

numero = (int)(input("Dime un número:"))
while numero != 0:
    suma = suma + numero
    media = media + 1
    numero = (int)(input("Dime otro número:))

print("La suma de todos lo números es:", suma, ", y su media es", media)
