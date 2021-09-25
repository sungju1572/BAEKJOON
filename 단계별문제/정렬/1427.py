import sys

a = sys.stdin.readline().rstrip()

a1 = "".join(sorted(a, reverse=True))
print(a1)

"""
간단하게 sorted 함수를 사용하여 구현하였다
"""