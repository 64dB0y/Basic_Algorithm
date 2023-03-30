#!/usr/bin/env python3
n = int(input())
result = [0] * n
for i in range(n):
    a, b = list(map(int, input().split())) 
    result[i] = a
    for j in range(b):
        # 매 곱셈마다 10으로 나눈것의 나머지만 계산하여 연산의 효율을 높인다
        result[i] = result[i] * a % 10
        if result[i]==0:
            result[i]=10

for k in range(n):
    print(result[k])