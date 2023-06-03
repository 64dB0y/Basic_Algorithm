def count_cards(card_nums, queries):
    card_counter = {}
    
    for num in card_nums:
        if num in card_counter: # card_counter에 이미 있는 문자인지 확인한다
            card_counter[num] += 1
        else:
            card_counter[num] = 1

    result = [card_counter[query] if query in card_counter else 0 for query in queries]
    return result

def main():
    card_count = int(input())
    card_nums = list(map(int, input().split()))
    query_count = int(input()) 
    queries = list(map(int, input().split()))

    result = count_cards(card_nums, queries)
    print(*result)

if __name__ == "__main__":
    main()
