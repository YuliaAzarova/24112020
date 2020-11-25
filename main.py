from time import*

start = time()
a, b, c, d,  = map(int, input().split())
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
otvet = 0
for x in range(1, 101):
    if a <= x <= b and c <= x <= d:
        otvet =otvet + 1
finish = time
print(otvet)