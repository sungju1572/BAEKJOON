a=int(input())

for i in range(a):
    d=0
    b= str(input())
    c=b.split("X")
    for j in range(len(c)):
        if len(c)>0:
            for h in range(len(c[j])):
                d+=(h+1)
    print(d)
                
