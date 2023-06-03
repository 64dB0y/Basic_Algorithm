import math

T = int(input())
results = []  # 결과를 저장할 리스트

for _ in range(T):
    N, M = map(int, input().split())

    result = math.comb(M, N)  # 조합 공식을 사용하여 결과를 바로 계산합니다.
    results.append(result)  # 결과를 리스트에 저장

# 결과 리스트를 한 번에 출력
for result in results:
    print(result)
