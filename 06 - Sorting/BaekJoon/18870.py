'''
1. 각 숫자를 입력 받는다
2. 
'''
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 좌표 압축 적용
coord = sorted(set(num))

# 좌표 압축 결과로 count 리스트를 만듦
count = [coord.index(x) for x in num]

print(*count)