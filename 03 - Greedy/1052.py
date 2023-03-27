'''
N(보유한 물병 갯수), K(빈 물병 최댓값) 값 각각 받습니다.
물병을 전부 세서 2진수로 변환합니다. -> 또한 1의 갯수를 셉니다.
N(보유한 물병 개수) = cnt(물이 들어있는 병 개수) + K (빈 병 개수)라는 사실을 인지하며 cnt가 K이하가 될때까지 상점에서 물병을 구매합니다.
'''
#!/usr/bin/env python3
# N = 보유한 물병 갯수
# K = 빈 물병 최대값
N, K = map(int, input().split())

def calculate_minimum_bottles(N, K):
    cnt = bin(N).count('1') # 이진수로 변환했을 때 1의 개수를 셉니다
    result = 0  # 상점에서 구매한 물병 개수
    while cnt > K: # N(보유한 물병 개수) = cnt(물이 들어있는 병 개수) + K (빈 병 개수)인걸 기억하자
        N += 1 # 물병을 구매합니다
        cnt = bin(N).count('1') # 구매한 물병을 합쳐서 1의 개수를 다시 셉니다
        result += 1 # 구매한 물병 개수를 증가시킵니다.
    return result

print(calculate_minimum_bottles(N, K))

'''
1   +   1   =   2   -> 1 0 (2)
2   +   2   =   4   -> 1 0 0 (2)
'''