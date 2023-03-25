'''
문제
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.

행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

입력
첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

출력
첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
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
