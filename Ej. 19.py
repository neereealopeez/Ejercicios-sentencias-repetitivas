def pintaMenu():
    opc=0
    while (opc<1 or opc>5):
        print("****MENÚ INICIAL****")
        print("1 - Insertar contacto")
        print("2 - Borrar contacto")
        print("3 - Buscar contacto")
        print("4 - Ver todos los contactos")
        print("5 - Salir")
        print("********************")

        try:
        opc= int(input("Selecciona un número "))
        if opc<1 or opc>5:
            print("Las opciones son del 1 al 5")


opc= pintaMenu()


