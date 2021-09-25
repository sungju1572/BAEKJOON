import sys
from collections import OrderedDict

a = int(sys.stdin.readline())

str_list = []
up_list = []

for i in range(a):
    b = sys.stdin.readline().strip()
    str_list.append([b, len(b)]) #문자,길이 순으로입력받음

str_list.sort(key= lambda x : (x[1], x[0])) #길이, 글자 순으로 정렬
 
#문자만 가져오기
for i in str_list: 
    up_list.append(i[0]) 

#리스트 중복제거하고 하나씩 출1력
for i in sorted(set(up_list), key = lambda x : up_list.index(x)):
    print(i)

"""
이번 문제를 풀면서 sort정렬에서 key를 사용할때, lambda 함수와 조합하여 두가지 조건을 한번에 쓸수 있다는것을 알았다
"""