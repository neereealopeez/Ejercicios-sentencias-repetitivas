productoAdquirido=10
meses=0
num=0
total=0

for num in range(1,21):
    meses=meses +1
    print(meses, "mes:", productoAdquirido, "euros")
    productoAdquirido= productoAdquirido*2
    total= total + productoAdquirido
print("En 20 meses el total pagado fue", total)