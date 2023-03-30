'''
n, m을 입력 받는다.
패키지 가격과 단품 가격을 m 횟수만큼 각각 작성한다.
패키지 가격 및 단품 가격을 입력 받을때 마다 각각 가장 최저 가격을 식별하여 저장한다.
모두 단품으로 샀을때, 단품 및 패키지를 섞어서 샀을때, 모두 패키지로 샀을 때 총 3가지 경우 중 가장 싸게 산걸 선택한다.
'''
# N, M을 입력받기
n, m = map(int, input().split())

# 이 문제는 배열에 저장할 필요가 없음. 매 입력마다 버릴 자료인지 아닌지 판단 가능 함.
# 특히 append도 시간에 영향을 주기도 하고, 메모리를 잡아먹기 때문에 상황을 잘 보고 안쓰는게 좋음

pkg = 1000
sgl = 1000

# M개의 줄에 대하여 묶음 가격과 낱개 가격을 입력받아 prices 리스트에 저장한다.
for _ in range(m):
    bundle, single = map(int, input().split())
    # prices.append((bundle, single))
    pkg = min(pkg, bundle)
    sgl = min(sgl, single)

ans = min(n*sgl, pkg*(n//6)+sgl*(n%6), pkg*((n//6)+1))
# 경우의 수 : 모든 줄을 낱개로, 낱개와 묶음을 섞어서, 모든 줄을 묶음으로

print(ans)