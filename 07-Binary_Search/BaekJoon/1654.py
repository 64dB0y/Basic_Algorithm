def find_optimal_length(target_count, each_len):
    low = 1
    high = max(each_len)

    result = 1
    while low <= high:
        mid = (low + high) // 2
        total_cable_count = sum([h // mid for h in each_len])

        if total_cable_count >= target_count:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

def main():
    cable_count, target_count = map(int, input().split())
    each_len = []
    for i in range(cable_count):
       length = int(input())
       each_len.append(length)
    
    result = find_optimal_length(target_count, each_len)
    print(result)

if __name__ == "__main__":
    main()