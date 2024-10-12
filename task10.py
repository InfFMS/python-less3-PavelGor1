def IsPrime(n):
    if n == 1:
        return 0
    d = 2
    while n % d != 0:
        d += 1
    return d == n
n = int(input())
a = []
for i in range(n):
    x = int(input())
    if IsPrime(x) == 1:
        a.append(x)
if len(a) == 0:
    print("0 0")
else:
    print(min(a), max(a))



