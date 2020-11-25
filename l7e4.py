ziro = 0
n = int(input())
for x in range(n):
    a = int(input())
    if a == 0:
        ziro = ziro + 1
if ziro > 0:
    print('YES')
else:
    print('NO')