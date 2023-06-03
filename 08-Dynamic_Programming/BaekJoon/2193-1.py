n = int(input())

# DP 테이블 초기화
dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = 0    # 길이가 1이고 마지막 자리 수가 0
dp[1][1] = 1    # 길이가 1이고 마지막 자리 수가 1

# DP 계산
for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

print(dp[n][0] + dp[n][1])  # 출력: 2
