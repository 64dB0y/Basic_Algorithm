'''
N, M에 행과 열 수를 입력한다.
matrix_a, matrix_b에 행렬을 저장한다.
flip 함수를 선언하여 1에서 0으로 바뀌도록 정의했다
check 함수를 선언하여 두 행렬이 같은지 확인하도록 정의했다.

35번 줄부터 실제로 두 행렬을 비교하여 서로 다르면 flip 함수를 사용하며 몇번 변환했는지 횟수가 증가합니다.
만약에 애초에 3x3행렬이 아니어서 변환할 수 없다면 -1을 반환합니다.
'''

#!/usr/bin/env python3
# N = row
# M = column
N, M = map(int, input().split())

# 행렬 A 입력 받기, M크기 만큼의 문자열을 N개 만큼 저장한다.
matrix_a = [list(map(int, input().strip()[:M])) for _ in range(N)]

# 행렬 B 입력 받기, M크기 만큼의 문자열을 N개 만큼 저장한다.
matrix_b = [list(map(int, input().strip()[:M])) for _ in range(N)]

# 기억 해야할건 똑같은 부분을 두번 뒤집으면 원래대로 돌아온다는 점을 기억하라
# 3x3 부분 행렬 뒤집기 함수
def flip(x, y, matrix):
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix[i][j] = 1 - matrix[i][j] 

# 두 행렬이 같은지 확인하는 함수
def check(matrix1, matrix2):
    for i in range(N):
        for j in range(M):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

count = 0 # 변환 횟수
# 3x3단위로 변환
for i in range(N-2):
    for j in range(M-2):
        if matrix_a[i][j] != matrix_b[i][j]:
            flip(i, j, matrix_a)
            count += 1

# 두 행렬이 같은지 확인
if check(matrix_a, matrix_b):
    print(count)
else:
    print(-1)
