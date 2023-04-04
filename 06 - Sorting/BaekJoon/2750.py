n = int(input()) # N 입력 받기
lst = []

for i in range(n):
    m = int(input()) # 수 입력 받기
    lst.append(m)

lst = sorted(lst)

for num in lst:
    print(num)