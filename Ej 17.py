'''
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Para esto, se registran los días que trabajó y las horas de cada día.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y
además calcule cuánto pagó la empresa por los N empleados
'''

empleados=0
horas=0
días=""
sueldoHoras=0
empresacobra=0
contador=0
sueldoSemanal=0

empleados=(int(input("¿Número de trabajadores? ")))
sueldoHoras=int(input("¿Cuánto cobras por hora? "))
for i in range (0,6):
    días=(input("¿Has trabajado hoy? "))
    if días=="si" or días=="sí":
        contador= contador + 1
        horas=int(input("¿Cuántas horas has trabajado hoy? "))

sueldoSemanal=sueldoSemanal+(sueldoHoras*horas*contador)
empresacobra= empleados*sueldoSemanal
print("El sueldo a la semana que recibe un trabajador de tu misma empresa es" ,sueldoSemanal)
print("La empresa paga un total de", empresacobra, "por los", empleados, " trabajadores de su empresa")