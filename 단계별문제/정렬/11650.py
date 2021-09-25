import sys

a = int(sys.stdin.readline())

xy_list  = []



for i in range(a):
    xy_list.append(list(map(int, sys.stdin.readline().split())))
    
    
for i in sorted(xy_list):
    print(i[0],i[1])


"""
이문제 역시 sorted함수를 사용해 간단하게 풀었다
"""