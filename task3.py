# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
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
print("Простых чисел:",p)
print("Составных чисел:",s)
