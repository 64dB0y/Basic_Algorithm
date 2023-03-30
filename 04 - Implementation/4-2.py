# N을 입력받기
n = int(input())
if n < 0 or n > 23:
    print("0<=N<=23의 값을 입력하세요.")
else:
    # 3이 들어 있는 시간대 횟수
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    print(count)