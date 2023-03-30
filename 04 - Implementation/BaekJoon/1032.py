'''
n 입력 받고
각 파일명 입력 받습니다
(어차피 모든 파일명이 동일하니까) 특정 파일명 길이만큼을 모두 ?로 채운 result 리스트를 선언합니다
특정 파일명을 기준으로 비교합니다.
'''
#!/usr/bin/env python3
n = int(input())
file = [input() for _ in range(n)]
result = ['?'] * len(file[0])
for i in range(len(file[0])):
    char = file[0][i]
    if all(f[i] == char for f in file[1:]):
        result[i] = char
print(''.join(result))