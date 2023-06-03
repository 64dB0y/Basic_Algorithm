def find_optimal_height(result_height, current_heights):
    low = 1
    high = max(current_heights)

    result = 1
    while low <= high:
        mid = (low + high) // 2
        total_wood = sum([h - mid if h > mid else 0 for h in current_heights])

        if total_wood >= result_height:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

def main():
    tree_count, result_height = map(int, input().split())
    current_heights = list(map(int, input().split()))
    result = find_optimal_height(result_height, current_heights)
    print(result)

if __name__ == "__main__":
    main()