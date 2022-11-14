horas=0
trabajadores=0
sueldoHora=0
sueldoSemanal=0
total=0

trabajadores=(int(input("¿Número de trabajadores? ")))
horas=(int(input("¿Cuántas horas trabajas diariamente? ")))
sueldoHora= (int(input("¿Cuánto cobras por hora? ")))

for i in range(1,6):
    sueldoSemanal=sueldoSemanal+(sueldoHora*horas)
total= trabajadores*sueldoSemanal
print("El sueldo a la semana que recibe un trabajador de tu misma empresa es" ,sueldoSemanal)
print("La empresa paga un total de", total, "por los", trabajadores, " trabajadores de su empresa")
