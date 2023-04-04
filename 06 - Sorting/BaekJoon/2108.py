'''
정수를 하나씩 입력받아 리스트 li에 추가한다.
각각 문제에서 요구하는 값들을 출력하는데
1. 산술평균 - 리스트 li의 모든 요소의 합을 수의 개수 n으로 나눈다.
2. 중앙값 - 리스트 li를 오름차순으로 정렬한 후 중간에 위치한 값을 출력한다.
3. 최빈값 - 리스트 li에서 가장 빈도수가 높은 값을 출력한다.
4. 범위 - 리스트 li에서 최댓값과 최솟값의 차이를 출력한다.
'''
import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))    # 정수를 하나씩 입력받아 리스트 li에 추가한다.
 
# 산술평균 - 다 더해서 / n
print(round(sum(li)/n))
 
# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n//2])
 
# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]:  # 최빈값이 2개 이상일 경우 두 번째로 작은 값을 출력한다.
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 - 최댓값-최솟값
print(max(li)-min(li))
