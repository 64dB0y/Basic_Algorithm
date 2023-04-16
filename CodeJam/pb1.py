'''
1. Colliding Encoding

문제
Alan은 학교에서 암호학 수업을 처음 들었다. 그는 배운 내용을 적용하여 자신만의 암호를 만들기로 결심했다. 그는 영어 알파벳의 각 문자를 0에서 9까지의 10진수 숫자에 매핑할 것이다. 그런 다음 각 단어를 인코딩하여 매핑된 숫자로 대체하여 10진수 숫자로 구성된 문자열로 인코딩하려고 한다.

그러나 Alan은 영어 알파벳에는 26개의 문자가 있고 10진수 숫자는 10개밖에 없다는 사실을 알아채지 못했다. 따라서 동일한 인코딩을 가진 서로 다른 단어 쌍이 발생할 수 있다.

Alan이 인코딩하려는 N개의 단어 목록과 사용하는 매핑이 주어졌을 때, 목록에서 단어 간 충돌이 있는지 확인할 수 있습니까?

입력

입력의 첫 번째 줄은 테스트 케이스 수 T를 나타내며, 그 다음 T개의 테스트 케이스가 이어진다.
각 테스트 케이스의 첫 번째 줄에는 Alan이 사용하는 매핑을 나타내는 26개의 10진수 숫자(DA, DB, ..., DZ)가 포함된다. 알파벳 문자 alpha는 Dalpha 숫자로 매핑된다.
각 테스트 케이스의 두 번째 줄에는 Alan이 인코딩할 단어의 수 N이 포함된다.
마지막 N줄 중 i번째 줄은 Alan이 인코딩할 i번째 단어를 나타내는 문자열 Si를 포함한다.

출력

각 테스트 케이스마다, 충돌이 있으면(목록에서 인코딩이 동일한 서로 다른 단어 쌍이 하나 이상 있는 경우) YES를, 그렇지 않으면 NO를 포함하는 Case #x: y라는 한 줄을 출력한다. 이때, x는 테스트 케이스 번호(1부터 시작)이고 y는 YES 또는 NO이다.

예시 입력
2
0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
4
ABC
BC
BCD
CDE
0 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
3
CDE
DEF
EFG

예시 출력

Case #1: NO
Case #2: YES
'''
#!/usr/bin/env python3
t = int(input())

results = []  # results 리스트를 초기화하여 선언합니다.

for i in range(1, t+1):
    mapping = input().split()
    n = int(input())
    words = []
    for j in range(n):
        words.append(input())

    # 숫자열을 key로, 인코딩된 단어를 value로 하는 딕셔너리를 생성합니다.
    code_dict = {}
    for word in words:
        code = ""
        for ch in word:
            code += mapping[ord(ch) - ord('A')]
        if code in code_dict:
            # 딕셔너리에 이미 같은 숫자열을 key로 가지는 인코딩된 단어가 존재하는 경우
            result = "YES"
            break
        else:
            code_dict[code] = word
    else:
        # 충돌이 없는 경우
        result = "NO"

    # 결과를 리스트에 추가합니다.
    results.append("Case #%d: %s" % (i, result))

# 모든 입력 처리가 완료된 후에 결과 리스트를 출력합니다.
for result in results:
    print(result)
