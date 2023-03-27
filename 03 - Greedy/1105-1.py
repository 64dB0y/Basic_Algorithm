'''
https://www.acmicpc.net/problem/1105

문제
L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 L과 R이 주어진다. L은 2,000,000,000보다 작거나 같은 자연수이고, R은 L보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.
'''
#!/usr/bin/env python3

#L, R 각각 입력 받기
while True:
    L, R = map(int, input().split())
    if 1 <= L <= 2000000000 and 1 <= R <= 2000000000:
        break
    print("입력 범위는 1 이상 2000000000 이하입니다.")

# min_cnt를 무한대로 초기화
min_cnt = float('inf')

for num in range(L, R+1):
    #cnt 안에 리스트 내 특정 원소의 8의 갯수를 센것을 넣겠다.
    cnt = str(num).count('8')
    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)