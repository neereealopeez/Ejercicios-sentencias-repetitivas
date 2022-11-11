ahorromes=0
ahorroaño=0
vAhorroMes=[]
for i in range (1,13):
    ahorromes=(int(input("¿Cuánta cantidad de dinero has ahorrado este mes? ")))
    ahorroaño=ahorromes+ahorroaño
    vAhorroMes=ahorroaño
    print("En total has ahorrado", vAhorroMes, "euros")
print("Este año ahorraste", ahorroaño, "euros")
