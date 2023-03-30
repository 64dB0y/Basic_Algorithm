'''
두 개의 정수 배열 A와 B를 입력 받는다.
A 배열을 오름차순으로 정렬한 후 B 배열에서 가장 큰 값을  차례대로 꺼내온다. (단, 꺼내올때 마다 꺼낸 B 배열의 원소는 제거)
A 배열의 요소와 곱한 뒤 더하여 결과를 출력한다.
'''
#!/usr/bin/env python3

# N을 입력받기
n = int(input())

# A, B 배열을 입력받기
a = list(map(int, input().split()))[:n]

b = list(map(int, input().split()))[:n]

# A 배열을 오름차순으로 정렬하기
a.sort()

# B 배열에서 가장 큰 수부터 차례대로 꺼내서 곱하기
result = 0
for i in range(n):
    result += a[i] * max(b)
    #곱셈 후에 사용한 B배열의 값은 제거한다
    b.remove(max(b))

print(result)