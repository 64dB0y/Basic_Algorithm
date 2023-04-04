'''
리스트 내에 어떤 값이 들어있는지 미리 정의한다.
반복문을 돌리면서 특정 인덱스의 값이 그 뒤에 리스트에 있는 값들과 비교하여 가장 작은 값이 해당 인덱스에 들어가도록 한다.
'''
#!/usr/bin/env python3
array = [7,5,9,0,3,1,6,2,4,8]
# 맨마지막에서 앞의 인덱스까지만 for문 돌리면 된다. 굳이, 맨 뒤 원소까지 갈 필요가 없다.
for curr_index in range(len(array)-1):
    target_index = curr_index
    # 현재 원소를 제외한 그 나머지 뒤에 있는 리스트들과 비교해서 누가 더 작은값을 갖는지 확인한다.
    for j in range(curr_index+1, len(array)):
        if array[target_index] > array[j]:
            target_index = j
    # 리스트의 원소를 서로 바꾼다.            
    array[curr_index], array[target_index] = array[target_index], array[curr_index]

print(array)
