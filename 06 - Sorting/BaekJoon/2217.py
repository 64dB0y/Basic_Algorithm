'''
내림차순으로 정렬하여 제일 중량이 큰거부터 차례대로 무게를 줄이면서 갯수는 늘린다
'''
import sys

n = int(sys.stdin.readline().strip())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=True)

max_weight = 0
for i in range(n):
    weight = li[i] * (i+1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)
