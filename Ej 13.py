horasdiarias=0
horastotal=0
sueldo=0
sueldo=int(input("¿Cuánto sueldo recibes por hora? "))

for i in range (0,6):
    horasdiarias=int(input("¿Cúantas horas has trabajado hoy? "))
    horastotal= horasdiarias+horastotal
sueldo=sueldo*horastotal
print("Tu sueldo total es", sueldo, "y el total de horas trabajadas es", horastotal)

