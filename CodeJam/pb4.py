'''
문제
Cody-Jamal은 생성 인공지능이 예술 작품을 만들어 내는 것을 들었습니다. 그는 새로운 예술의 기회에 흥분하지만, 동시에 인간이 창작한 예술이 밀려날까 걱정하고 있습니다. 그는 컴퓨터를 사용하여 인간이 단순히 만들 수 없는 예술 작품을 창작하는 것이 좋은 타협점이 될 것이라고 생각했습니다.

Cody-Jamal은 컴퓨터 생성 예술에 처음 입문하는 중이므로 간단하게 시작했습니다. 그는 영어 알파벳을 두 번 반복하는 방식으로 거대한 문자열을 생성하여 그 일상성과 영속성을 나타내고자 합니다.

Cody-Jamal은 다음 프로그램을 작성했습니다.

for i = 1 to 1e100:
for letter = A to Z:
print letter i times
여기서 1e100은 정수 10^100을 나타냅니다. 예를 들면:

i=1일 때 프로그램은 ABCD....XYZ를 출력합니다.
i=2일 때 프로그램은 AABBCC...XXYYZZ를 출력합니다.
i=3일 때 프로그램은 AAABBBCCC...XXXYYYZZZ를 출력합니다.
물론 Cody-Jamal의 프로그램은 끝나기까지 오랜 시간이 걸립니다. 그가 출력되기를 기다리지 않고 N번째 인쇄 문자가 무엇인지 알려주실 수 있나요?

입력
입력의 첫 줄에는 테스트 케이스 수 T가 주어집니다. T개의 테스트 케이스가 이어집니다.
각 테스트 케이스는 정수 N이 하나의 줄로 구성되어 있습니다.

출력
각 테스트 케이스마다 Case #x: y 형식으로 한 줄을 출력합니다. 여기서 x는 테스트 케이스 번호(1부터 시작)이고 y는 Cody-Jamal의 프로그램에서 인쇄된 N번째 문자입니다.
'''
def find_nth_letter(n):
    i = 1
    # i와 (i + 1) // 2의 곱에 26을 곱한 값이 n보다 작은 동안 반복합니다.
    while (i * (i + 1) // 2) * 26 < n:
        i += 1

    # 이전 단계에서 계산한 값을 n에서 빼줍니다.
    n -= ((i - 1) * i // 2) * 26

    # 알파벳 중 몇 번째 글자인지 구합니다.
    letter_index = (n - 1) // i
    # 해당 인덱스의 알파벳 글자를 구합니다.
    letter = chr(ord('A') + letter_index)

    return letter


def main():
    # 테스트 케이스의 수를 입력받습니다.
    t = int(input().strip())
    results = []
    # 각 테스트 케이스에 대해 처리합니다.
    for _ in range(t):
        # N을 입력받습니다.
        n = int(input().strip())
        # N번째 글자를 구하는 함수를 호출합니다.
        result = find_nth_letter(n)
        # 결과를 리스트에 추가합니다.
        results.append(result)

    # 결과 리스트를 출력합니다.
    for x, result in enumerate(results, start=1):
        print(f"Case #{x}: {result}")


if __name__ == "__main__":
    main()
