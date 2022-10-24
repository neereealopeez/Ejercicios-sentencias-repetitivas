num=0
resultado=1
num=int(input("Número: "))
for num in range(1,num+1):
	resultado= resultado*num
print("El factorial de es", num, "es", resultado)