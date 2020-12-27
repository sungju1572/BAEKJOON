a = int(input())
for i in range(a):
    d=[]
    b= list(map(int, input().split()))
    b.pop(0)
    c= sum(b, 0.0)/len(b)
    for j in range(len(b)):
        if b[j]>c:
            d.append(b[j])
    print(format(len(d)/len(b)*100,".3f"),"%",sep="")
            
