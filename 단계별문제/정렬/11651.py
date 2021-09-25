import sys

a = int(sys.stdin.readline())

xy_list = []

for i in range(a):
    x,y = map(int, sys.stdin.readline().split())
    xy_list.append([y,x])


for i in sorted(xy_list):
    print(i[1], i[0])

"""
11650번 문제와 유사하게 x,y입력값만 다르게 받아 정렬하여 출력하였다
"""