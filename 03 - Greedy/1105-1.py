'''
L과 R의 입력 범위를 지정합니다.
min_cnt를 무한으로 초기화합니다.
L과 R 사이의 범위에 있는 숫자 들 중에 8의 개숫를 string으로 변환하여 cnt에 저장합니다. 
만약 cnt가 min_cnt보다 작다면 cnt내 값을 min_cnt로 저장합니다.
'''
#!/usr/bin/env python3

#L, R 각각 입력 받기
while True:
    L, R = map(int, input().split())
    if 1 <= L <= 2000000000 and 1 <= R <= 2000000000:
        break
    print("입력 범위는 1 이상 2000000000 이하입니다.")

# min_cnt를 무한대로 초기화
min_cnt = float('inf')

for num in range(L, R+1):
    #cnt 안에 리스트 내 특정 원소의 8의 갯수를 센것을 넣겠다.
    cnt = str(num).count('8')
    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)