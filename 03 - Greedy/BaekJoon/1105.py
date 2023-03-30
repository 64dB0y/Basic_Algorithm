'''
https://www.acmicpc.net/problem/1105
L과 R 사이의 범위를 저장합니다.
L과 R 사이의 모든 값을 리스트 안에 저장합니다.
리스트 내의 모든 원소들에 대하여 8의 갯수를 따지고 그걸 딕셔너리에 저장합니다.
딕셔너리를 정렬한 후 가장 적게 나온 8의 갯수를 출력합니다.
'''
#!/usr/bin/env python3

#L, R 각각 입력 받기
while True:
    L, R = map(int, input().split())
    if 1 <= L <= 2000000000 and 1 <= R <= 2000000000:
        break
    print("입력 범위는 1 이상 2000000000 이하입니다.")

# L 이상 R 이하의 모든 자연수를 담은 리스트 lst가 있다고 가정합니다.
lst = [i for i in range(L, R+1)]

# 딕셔너리에 각 숫자에 대한 8의 개수를 저장합니다.
cnt_dict = {}
for num in lst:
    cnt = str(num).count('8')
    cnt_dict[num] = cnt

# 딕셔너리를 정렬한 후, 가장 적게 나온 8의 개수를 반환합니다.
min_cnt = min(cnt_dict.values())

print(min_cnt)