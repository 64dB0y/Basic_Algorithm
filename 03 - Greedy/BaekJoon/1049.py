'''
https://www.acmicpc.net/problem/1049
N, M 각 각 입력받고, 각 세트 및 낱개 가격을 한 세트로 묶어서 prices 리스트에 저장한다.
리스트에 저장되어 있는 가격들 중 세트 가격이 가장 싼 걸 고른다
리스트에 저장되어 있는 가격들 중 낱개 가격이 가장 싼 걸 고른다
낱개로만 구매했을 경우와 세트와 낱개 모두를 섞어서 계산했을 경우 중 어느것이 더 싸게 구매한건지를 따진다
'''
#!/usr/bin/env python3
# N, M을 입력받기
n, m = map(int, input().split())

prices = []

# M개의 줄에 대하여 묶음 가격과 낱개 가격을 입력받아 prices 리스트에 저장한다.
for _ in range(m):
    bundle, single = map(int, input().split())
    prices.append((bundle, single))

# 6개씩 살 때 가장 싼 가격으로 계산
six_price = min([price[0] for price in prices])
# 낱개로만 살 때 가장 싼 가격으로 계산
single_price = min([price[1] for price in prices])

# 6개 패키지로만 최대한 구매한 뒤, 남은 것을 낱개로 살 경우의 가격
ans = (n // 6) * six_price + min((n % 6) * single_price, six_price)

result = min(ans, single_price*n)
print(result)