vNum = []
numero= 0
menorcont = 0
mayorcont = 0
igualcont=0
cantidad = (int)(input("Dime la cantidad de números que vas a introducir: "))

for i in range(1,cantidad):
    numero = (int)(input("Dime un número:\n"))
    vNum.append(numero)

for i in vNum:
    if i==0:
        igualcont+=1
    elif i<0:
        menorcont+=1
    elif i>0:
        mayorcont+=1

print("Hay:", mayorcont, "numeros mayores que 0, ", igualcont, "iguales que 0 y", menorcont, "menores de 0")