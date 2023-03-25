# N, M을 입력받기
n, m = map(int, input().split())

# 이 문제는 배열에 저장할 필요가 없음. 매 입력마다 버릴 자료인지 아닌지 판단 가능 함.
# 특히 append도 시간에 영향을 주기도 하고, 메모리를 잡아먹기 때문에 상황을 잘 보고 안쓰는게 좋음
# prices = []

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