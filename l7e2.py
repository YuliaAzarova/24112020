n = int(input())
for x in range(100, 1000):
    b = x // 100
    c = (x - b * 100)//10
    d = (x - b*100-c*10)//1
    e = b+c+d
    if e == n:
        print(x)