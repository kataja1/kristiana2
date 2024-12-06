import random
n=5
lielaka_summa=0
for i in range(n):
    a=random.randint(1, 6)
    b=random.randint(1, 6)
    print (a,b, a+b)

    if (a+b)>lielaka_summa:
        lielaka_summa= a+b
        print()

    if(a+b)> lielaka_summa:
        lielaka_summa =(a+b)

print(f"Lielākā summas vērtība: {lielaka_summa}")
print(f"summa{a}")
    

