#!/usr/bin/env python3

N, M = map(int, input().split())

matrix_a = [list(map(int, input().strip()[:M])) for _ in range(N)]
matrix_b = [list(map(int, input().strip()[:M])) for _ in range(N)]

def flip(x, y, matrix):
    matrix_c = [row[:] for row in matrix]
    for i in range(x, x+3):
        for j in range(y, y+3):
            matrix_c[i][j] = 1 - matrix_c[i][j]
    return matrix_c

def check(matrix1, matrix2):
    for i in range(N):
        for j in range(M):
            if matrix1[i][j] != matrix2[i][j]:
                return False
    return True

count = 0
for i in range(N-2):
    for j in range(M-2):
        if matrix_a[i][j] != matrix_b[i][j]:
            matrix_a = flip(i, j, matrix_a)
            count += 1

if check(matrix_a, matrix_b):
    print(count)
else:
    print(-1)
