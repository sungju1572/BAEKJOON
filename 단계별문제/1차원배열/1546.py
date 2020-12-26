N=int(input())
a= list(map(int, input().split()))
b=[]
for i in range(N):
    b.append((a[i]/max(a))*100)
    
print(sum(b,0.0)/N)
