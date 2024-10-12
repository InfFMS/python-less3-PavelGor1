n = int(input())
p = 0
while n!=0:
    for i in range(2,n):
        a = 0
        for j in range(2,i+1):
            if i%j==0:
                a +=1
        if a==1:
            print(i)