N = input()
N1=N
if int(N1)<10:
    N1="0"+N1 

N2=N1

a=1
while True:
    N2 = N2[-1]+str(int(N2[0])+int(N2[-1]))[-1]
    if N2==N1:
        break
    a+=1
print(a)
