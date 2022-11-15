import time

horas=0
mins=0
seg=0

for h in range (24):
    for m in range(60):
        for s in range(60):
            print(h,":", m, ":",s)
            for i in range(7):
                print()
            time.sleep(1)