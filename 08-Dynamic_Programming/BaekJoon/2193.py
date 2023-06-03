from itertools import product

def is_pinary_number(temp_list):
    if temp_list[0] == 0:  # 이친수는 0으로 시작하지 않음
        return False
    for i in range(len(temp_list) - 1):
        if temp_list[i] == 1 and temp_list[i+1] == 1:  # 이친수에서는 1이 두 번 연속으로 나타나지 않음
            return False
    return True

n = int(input())
temp_lists = list(product([0,1], repeat=n))
count = 0

for temp_list in temp_lists:
    if is_pinary_number(temp_list):
        count += 1

print(count)