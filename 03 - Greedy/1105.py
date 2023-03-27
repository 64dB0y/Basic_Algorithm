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

# L 이상 R 이하의 모든 자연수를 담은 리스트 lst가 있다고 가정합니다.
lst = [i for i in range(L, R+1)]

# 딕셔너리에 각 숫자에 대한 8의 개수를 저장합니다.
cnt_dict = {}
for num in lst:
    cnt = str(num).count('8')
    cnt_dict[num] = cnt

# 딕셔너리를 정렬한 후, 가장 적게 나온 8의 개수와 그 개수를 가진 숫자들을 반환합니다.
min_cnt = min(cnt_dict.values())

print(min_cnt)