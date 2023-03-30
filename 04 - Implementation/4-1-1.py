'''
N을 입력받게 한다
이동방향을 담을 리스트(direction)를 선언한다.
시작 지점 (1,1)을 지정한다.
조건문을 확인하고 조건에 부합하면 계산하여 결과를 출력한다.
'''
#!/usr/bin/env python3

# N을 입력받기
n = int(input())

# 이동방향을 문자로 입력 받게 한다.
direction = list(map(str, input().split()))

# 이동 횟수가 100 이하인지 확인
if len(direction) > 100:
    print("Error: 이동 횟수가 100을 초과합니다.")

else:
    # 시작 지점
    start_point = [1, 1]
    # 시작 지점을 임시로 받기 위해 선언
    start_point2 = start_point[:]

    for i in range(len(direction)):
        if direction[i] == 'L': # left
            start_point2[1] -= 1
        elif direction[i] == 'R':   # right
            start_point2[1] += 1
        elif direction[i] == 'U':   # up
            start_point2[0] -= 1
        elif direction[i] == 'D':   # down
            start_point2[0] += 1

        # 공간을 벗어나는 경우 무시
        if start_point2[0] < 1 or start_point2[0] > n or start_point2[1] < 1 or start_point2[1] > n:
            start_point2 = start_point[:]
        else:
            start_point = start_point2[:]

    print(start_point[0], start_point[1])