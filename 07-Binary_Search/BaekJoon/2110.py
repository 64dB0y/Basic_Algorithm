def adjacent_distance(adapter_count, house_addr):
    low = 1  
    high = house_addr[-1] - house_addr[0]  # 가장 멀리 떨어진 두 집 사이의 거리
    result = 0

    while low <= high:
        mid = (low + high) // 2  
        installed_adapters = 1  # 첫 번째 집에는 항상 공유기를 설치한다고 가정
        current_house = house_addr[0]

        # 공유기를 설치할 수 있는 집을 확인
        for i in range(1, len(house_addr)):
            if house_addr[i] - current_house >= mid:  # 현재 집에서의 거리가 중간 거리 이상인 경우
                installed_adapters += 1  # 공유기를 설치
                current_house = house_addr[i]  # 현재 집을 업데이트

        # 공유기의 개수가 목표 개수 이상인 경우
        if installed_adapters >= adapter_count:
            result = mid  # 현재 중간 거리를 결과로 저장
            low = mid + 1  # 최소 거리를 높여서 범위를 좁힘
        else:
            high = mid - 1  # 최대 거리를 줄여서 범위를 좁힘

    return result

def main():
    house_count, adapter_count = map(int, input().split())
    house_addr = []
    for i in range(house_count):
        length = int(input())
        house_addr.append(length)
    
    house_addr.sort()  # 집의 좌표를 정렬
    result = adjacent_distance(adapter_count, house_addr)
    print(result)

if __name__ == "__main__":
    main()
