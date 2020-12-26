a=[]
for i in range(10):
    a.append(int(input()))
    
b=[]
for i in range(len(a)):
    b.append(a[i]%42)

d=0
for i in range(42):
    if b.count(i)==1:
        d+=1
    elif b.count(i)>=2:
        d+=1
print(d)
