import random
numero= random.randint(1,100)
escrito=0
intentos=1
escrito=int(input("Número: "))

while intentos !=10 and escrito!=numero:
    if escrito<numero:
        print("El número introducido es menor que el número secreto.")
       
    elif escrito>numero:
        print("El número introducido es mayor que el número secreto")
        
    escrito=(int(input("Número: ")))
    intentos= intentos + 1
    print("Llevas", intentos, "intentos")  


if escrito==numero:
    print("Has acertado")
else:
    print("Has llegado al límite de intentos, el número era", numero)

