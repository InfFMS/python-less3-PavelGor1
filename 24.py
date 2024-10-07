x = int(input())
p = 0
s = 0
while x != 0:
    p1 = 0
    for i in range(1,x+1):
        if x%i==0:
            p1+=1
    if p1==2:
        p += 1
    else: s+=1
    x = int(input())
print(s)
print(p)
