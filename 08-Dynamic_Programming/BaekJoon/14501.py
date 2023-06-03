'''
1. 어떤 경우에도 상담 전체 날짜를 넘어가면 안된다.
2. 상담을 한다면 해당 날짜 + 상담에 필요한 날짜 수가 전체 날짜 수를 넘기는 일은 일어나선 안된다.
3. dp 리스트를 사용하여 중복되는 부분 문제들을 저장해 둔다.
'''

def max_payment(index):
    if index >= n:
        return 0
    if dp[index] != -1:
        return dp[index]
    
    # 상담을 하는 경우
    if index + time_and_pay[index][0] <= n:
        dp[index] = max(dp[index], time_and_pay[index][1] + max_payment(index + time_and_pay[index][0]))

    # 상담을 하지 않는 경우
    dp[index] = max(dp[index], max_payment(index + 1))

n = int(input())
time_and_pay = []
for _ in range(n):
    time, pay = map(int, input().split())
    time_and_pay.append((time, pay))

dp = [-1] * n
Max_payment = max_payment(0)
print(Max_payment)