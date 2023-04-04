'''
리스트 내에 어떤 값이 들어있는지 미리 정의한다.
인덱스가 가장 낮은 순서부터 인덱스를 점차 확장해 가면서 
그때마다 새로 추가된 데이터와 정렬된 데이터와 비교하여 알맞는 인덱스에 새로 추가된 데이터를 넣습니다.
'''
#!/usr/bin/env python3
array = [7,5,9,0,3,1,6,2,4,8]

#가장 낮은 인덱스 부터 인덱스를 점차 늘립니다.
for i in range(1, len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
