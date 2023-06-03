'''
1. 테스트 케이스 입력받고, 각 테스트 케이스에 대한 결과를 저장할 리스트 선언
2. T 만큼 테스트 케이스 반복하면서 N, M 입력 받는다.
3. dp 테이블 초기화
4. 왼쪽이 한개만 있을때 문조건 오른쪽에 있는 갯수만큼 케이스 있으니 수정
5. 왼쪽 오른쪽 갯수 같을때는 케이스가 1로만 나와야만 한다
6. j개의 원소중 마지막 원소를 포함/제외 하여, i개 선택
'''
T = int(input())

results = []

for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0]*(M+1) for _ in range(N+1)]

    # DP 테이블 초기화 수정
    for i in range(1, M+1):
        dp[1][i] = i

    # DP 계산
    for i in range(2, N+1):
        for j in range(i, M+1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    results.append(dp[N][M])

for result in results:
    print(result)