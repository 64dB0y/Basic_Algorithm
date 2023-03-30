'''
밑수가 1, 5, 6 일때는 몇번을 곱해도 밑수다.
4, 9는 지수가 1의 배수냐 2의 배수냐에 따라 결과가 달라진다.
그 외의 자연수가 밑수인 경우에는 4를 주기로 반복한다.
'''
#!/usr/bin/env python3
n = int(input())
result = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    if not (1 <= a < 100) or not (1 <= b < 1000000):
        continue
    result[i] = a
    if a == 1 or a == 5 or a == 6:
        result[i]=a
    elif a == 4 or a == 9:
        b = b % 2
        result[i] = (a ** b) % 10
    else:
        b=b%4
        result[i]=(a**b)%10

for k in range(n):
    print(result[k])