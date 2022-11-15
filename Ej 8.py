limiteinf=0
limitesup=0
cont_fuera_intervalo =0
suma_dentro_intervalo =0
igual_limites=0

limiteinf = int(input("Dime el límite inferior del intervalo: "))
limitesup = int(input("Dime el límite superior del intervalo: "))
while limiteinf > limitesup:
    print("El límite inferior no puede ser mayor al superior.")
    limiteinf= int(input("Dime el límite inferior del intervalo: "))
    limitesup = int(input("Dime el límite superior del intervalo: "))

num = int(input("Dime un número: "))
while num!=0:
    if num>limiteinf and num<limitesup: 
        suma_dentro_intervalo =suma_dentro_intervalo + num
    else: 
        cont_fuera_intervalo = cont_fuera_intervalo + 1
        if num==limiteinf or num==limitesup:
            igual_limites = True
    num = int(input("Dime un número: "))


print(f"La suma de los números dentro del intervalo es {suma_dentro_intervalo}")
print(f"La cantidad de números fuera del intervalo es {cont_fuera_intervalo}")
if igual_limites:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")