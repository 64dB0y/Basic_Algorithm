'''
N을 입력 받는다.
시->분->초 순서로 3이 있는지 확인을 진행한다
(이때, 초를 제외한 나머지 단위는 3이 발견되면 굳이 아래까지 확인하지 않고 갯수를 센다)
'''
#!/usr/bin/env python3

# N을 입력받기
n = int(input())
if n <0 or n > 23:
    print("0<=N<=23의 값을 입력하세요.")
else:
    # 3이 들어 있는 시간대 횟수
    count = 0
    for i in range(n+1):
        # "시" 단위에서 3을 찾으면 그 하위 단위는 굳이 계산하지 말고 넘어가라
        if '3' in str(i):
            count += 3600
        else:
            for j in range(60):
                # "분" 단위에서 3을 찾으면 그 하위 단위는 굳이 계산하지 말고 넘어가라
                if '3' in str(j):
                    count += 60
                else:
                    for k in range(60):
                        if '3' in str(k):
                            count += 1
    
    print(count)