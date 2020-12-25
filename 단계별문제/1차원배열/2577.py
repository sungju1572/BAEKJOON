a=[]
for i in range(3):
    a.append(int(input()))
b= a[0]*a[1]*a[2]

c=[]
for x in range(len(str(b))):
       c.append(int(str(b)[x]))

for y in range(10):
    print(c.count(y))
