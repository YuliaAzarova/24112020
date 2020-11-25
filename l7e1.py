summa = 0
for x in range(1000, 10000):
    a = x//1000
    b = (x - a * 1000)//100
    c = (x - a * 1000 - b * 100)//10
    d = (x - a * 1000 - b*100-c*10)//1
    e = a + b+c + d
    if e == 20:
        summa = summa + x
print(summa)