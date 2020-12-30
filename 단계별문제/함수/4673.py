def kap(a):
    a= str(a)
    b= int(a)
    if len(a)==1:
        a= "0"+a
        for i in range(len(a)):
            b+= int(a[i])
    else : 
        for i in range(len(a)):
            b+= int(a[i])
    return int(b)

c=list(range(1,10000))
d=[]
for i in c:
    if kap(i)<10000:
        d.append(kap(i))
e=[]
for i in d:
    if i not in e:
        e.append(i)
f=[]
for i in c:
    if i not in e:
        f.append(i)

for i in f:
    print(i)
