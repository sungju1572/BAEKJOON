import sys
from collections import Counter

def rounded(list): #반올림
    return round(sum(list)/len(list))

def median(list, n):#중앙값
    list.sort()
    return list[int(n/2)]

def mode(list):#최빈값
    mode_dict = Counter(list)
    modes = mode_dict.most_common()    
    if len(list) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

def ranged(list):#범위
    return max(list)-min(list)

n = int(sys.stdin.readline())

num_list = [int(sys.stdin.readline().strip()) for i in range(n)]

print(rounded(num_list))
print(median(num_list,n))
print(mode(num_list))
print(ranged(num_list))

"""
메모리에 신경써야하는 문제들은 input 대신 sys.stdin.readline()를 쓰는것이 바람직하다
하지만 주피터 노트북에선 sys.stdin.readline()이 구동되지 않아, VS code 를 사용하기로 했다

이문제는 간단하게 각 함수를 만들면 될줄 알았지만, 메모리를 신경써야 된다는 점에서 살짝 까다로웠다
다른부분은 쉽게 했지만 최빈값 구하는 부분에서 메모리 오류가 계속 나서 구글링한결과 collections 모듈의 Counter 클래스를 알게되었다
문자열이나, 리스트에서 최빈값을 뽑아 딕셔너리 구조로 반환해주는 함수이다

counter를 사용하여 메모리 초과가 나지않고 성공하였다
"""