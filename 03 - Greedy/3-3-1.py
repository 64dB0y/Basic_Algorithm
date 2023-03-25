#!/usr/bin/env python3

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# n개의 행을 가지는 2차원 리스트 생성
array = [[] for _ in range(n)]
# 각 행에서의 최소값을 저장할 리스트
min_values = []
for i in range(n):
    # m개의 수를 공백으로 구분하여 입력받기
    row = list(map(int, input().split()))[:m]
    array[i] = row
    # 행에서 최소값 찾아서 리스트에 추가하기
    min_value = min(row)
    min_values.append(min_value)

# 최소값 중 가장 큰 값 찾기
result = max(min_values)

print(result)