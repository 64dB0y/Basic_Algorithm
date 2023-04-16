'''
2. Illumination Optimization

문제
Onyaomale은 고에너지 효율성과 강력함을 가진 LED 전구로 고속도로 불빛을 대체하는 프로젝트를 주도하고 있습니다. 프로젝트의 첫 단계는 모든 구형 백열 전구를 제거하는 것이었고, 이제는 새로운 LED 전구를 설치하는 데 집중하고 있습니다. 새로운 전구는 더욱 강력하기 때문에, Onyaomale은 몇몇 가로등이 필요 없어질 수 있다고 생각하며 더 많은 에너지 절약을 할 수 있을 것이라고 생각합니다.

고속도로를 서부에서 동부로 향하는 길이가 M 미터인 직선으로 모델링합니다. x번째 미터는 고속도로 서쪽 끝에서 x 미터 동쪽에 위치한 지점입니다. 거리 x에 가로등이 위치하고, 조명 반경이 R 미터인 전구가 설치되면, 가로등은 max(0, x-R)번째 미터부터 min(M, x+R)번째 미터까지를 포함하는 고속도로 구간을 조명합니다. Onyaomale은 모든 고속도로 구간이 하나 이상의 가로등에 의해 조명되도록 전구를 설치해야 합니다. 이에는 고속도로 끝점에서 정수 거리에 떨어지지 않는 점도 포함됩니다. 전구가 없는 가로등은 아무것도 조명하지 않습니다.

고속도로 길이인 M, 새로운 전구의 조명 반경인 R 및 모든 가로등의 위치가 주어지면 Onyaomale이 전체 고속도로를 조명하기 위해 설치해야 할 최소 전구 수를 찾거나 조명 할 수 없으면 IMPOSSIBLE을 보고합니다.

입력 형식

첫 번째 줄에는 테스트 케이스의 수 T가 주어집니다. 그 후 T개의 테스트 케이스가 따릅니다.
각 테스트 케이스는 두 줄로 구성됩니다. 첫째 줄에는 고속도로의 길이 M(m), 전구의 조명 반경 R(m) 및 가로등의 수 N이 들어 있습니다. 둘째 줄은 N개의 정수 X1, X2, ..., Xn을 포함합니다. 이는 가로등이 위치한 고속도로 미터의 위치를 나타냅니다.

출력 형식

각 테스트 케이스에 대해 "Case #x: y"를 출력합니다. 여기서 x는 각 테스트 케이스에 대해 "Case #x: y"를 출력합니다. 여기서 x는 테스트 케이스 번호(1부터 시작), y는 전체 고속도로를 조명하기 위해 Onyaomale이 설치해야 하는 최소한의 전구 수입니다. 전체 고속도로를 조명하는 방법이 없는 경우, y는 IMPOSSIBLE입니다.

제한 사항

시간 제한: 10초
메모리 제한: 2GB
1 ≤ T ≤ 100
1 ≤ M ≤ 10^9
1 ≤ R ≤ 10^9
0 ≤ Xi
Xi < Xi+1 (i < N)
XN ≤ M
서브태스크 1(visible Verdict): 1 ≤ N ≤ 10
서브태스크 2(visible Verdict): 1 ≤ N ≤ 10^5

샘플 입력

3
10 3 3
2 7 9
10 2 3
2 7 9
10 2 4
2 3 7 9

샘플 출력

Case #1: 2
Case #2: IMPOSSIBLE
Case #3: 4
'''
'''
풀이

1. 테스트 케이스 수를 입력 받는다.
2. 각 테스트 케이스에 대해 입력을 받고, test_cases 리스트에 저장한다.
3. min_bulbs_required 함수를 호출하여 각 테스트 케이스에 대한 결과를 계산한다.
4. 결과를 출력 형식에 맞추어 출력한다.
'''
'''
min_bulbs_required 함수는 다음과 같은 로직으로 동작합니다:

1. 각 테스트 케이스에 대해, 고속도로 길이(M), 전구의 조명 반경(R), 가로등의 수(N) 및 가로등 위치(street_lights)를 입력으로 받습니다.
2. 가로등 위치를 오름차순으로 정렬합니다.
3. 설치해야 하는 전구의 수를 저장할 변수(bulbs)와 현재 확인 중인 가로등 위치의 인덱스(i)를 초기화하고, 현재 조명 범위의 오른쪽 끝을 나타내는 변수(coverage)를 0으로 설정합니다.
4. 전체 고속도로가 조명되지 않은 동안 다음 과정을 반복합니다:
    a. 현재 확인 중인 가로등 위치가 조명 범위 내에 있으면 인덱스를 증가시킵니다.
    b. 조명 범위 내에 있는 가로등이 없거나 그 가로등의 조명 범위가 현재 조명 범위를 넘어서지 않으면 조명이 불가능하다고 판단하고 "IMPOSSIBLE"을 결과로 설정한 후 반복을 종료합니다.
    c. 조명 범위를 확장하고 전구의 수를 증가시킵니다.
5. 결과 리스트에 현재 테스트 케이스의 결과를 추가합니다.
6. 모든 테스트 케이스에 대한 결과 리스트를 반환합니다.
'''
#!/usr/bin/env python3
def min_bulbs_required(T, test_cases):
    results = []  # 각 테스트 케이스에 대한 결과를 저장할 리스트

    # 각 테스트 케이스에 대해
    for t in range(T):
        M, R, N, street_lights = test_cases[t]
        street_lights.sort()  # 가로등 위치를 오름차순으로 정렬

        bulbs = 0  # 설치해야 하는 전구의 수
        i = 0  # 현재 확인 중인 가로등 위치의 인덱스
        coverage = 0  # 현재 조명 범위의 오른쪽 끝

        # 전체 고속도로가 조명되지 않은 동안 반복
        while coverage < M:
            # 현재 확인 중인 가로등 위치가 조명 범위 내에 있으면 인덱스를 증가시킴
            if i < N and street_lights[i] - R <= coverage:
                i += 1
            else:
                # 조명 범위 내에 있는 가로등이 없거나 그 가로등의 조명 범위가
                # 현재 조명 범위를 넘어서지 않으면 조명이 불가능하다고 판단
                if i == 0 or street_lights[i - 1] + R <= coverage:
                    bulbs = "IMPOSSIBLE"
                    break
                # 조명 범위를 확장하고 전구의 수를 증가시킴
                coverage = street_lights[i - 1] + R
                bulbs += 1

        results.append(bulbs)  # 결과 리스트에 현재 테스트 케이스 결과를 추가

    return results  # 결과 리스트 반환

def main():
    T = int(input())  # 테스트 케이스 수 입력 받기
    test_cases = []  # 테스트 케이스 저장할 리스트

    # 각 테스트 케이스에 대한 입력 받기
    for _ in range(T):
        M, R, N = map(int, input().split())
        street_lights = list(map(int, input().split()))
        test_cases.append((M, R, N, street_lights))

    # min_bulbs_required 함수를 이용하여 결과 계산
    result = min_bulbs_required(T, test_cases)

    # 결과 출력
    for i, res in enumerate(result):
        print(f"Case #{i+1}: {res}")

if __name__ == "__main__":
    main()
