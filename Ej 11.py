num=0
raiz=0
divisible=0
numero=0

num=int(input("Dime un número"))
raiz=num**(1/2)

for numer in range (0, raiz):
    if(num%numero==0):
        divisible= divisible + 1
if (divisible==1):
    print(num, "es primo")
else:
    print(num, "no es primo")
