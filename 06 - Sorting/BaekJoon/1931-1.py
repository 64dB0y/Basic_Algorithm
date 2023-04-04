'''
n, 시작-종료 시간을 각각 받습니다.
종료시간을 기준으로 정렬을 합니다. -> 정렬한걸 유지한채로 앞도 정렬
종료 시간이 시작시간보다 작거나 같으면 횟수를 1회 증가합니다. (단, 종료시간을 계속 저장해둠으로써 각 for문을 돌때마다 없데이트 합니다)
결론은 가장 횟수가 많은것이 출력됩니다
'''
n = int(input().strip())
result = []
end_time = 0
count = 0
MAX_COUNT = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    result.append((a, b))

result=sorted(result, key=lambda x: (x[1], x[0])) # 뒷자리 먼저 정렬하고 앞자리를 정렬할 수 있다

for j in range(len(result)):
    if end_time <= result[j][0]:
        end_time = result[j][1]
        count += 1
        if MAX_COUNT < count:
            MAX_COUNT = count
    elif end_time == result[j][1] and end_time == result[j][0]:
        end_time = result[j][1]
        count += 1
        if MAX_COUNT < count:
            MAX_COUNT = count

print(MAX_COUNT)