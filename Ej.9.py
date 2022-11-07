
from cgitb import reset
from email.encoders import encode_base64


base=0
exp=0
resultado=1
base= (float)(input("Dime la base "))
exp=(int)(input("Dime el exponente "))
if exp<0:
    print("El exponente debe ser positivo")
    exp=(int)(input("Dime el exponente"))  
for i in range(0,exp):
    resultado=resultado*base  
printb n("Potencia=", resultado)