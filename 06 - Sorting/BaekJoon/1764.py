import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
no_listen = []
no_watch = []
for _ in range(n):
    no_listen.append(sys.stdin.readline().strip())    # 정수를 하나씩 입력받아 리스트 no_listen에 추가한다.

for _ in range(m):
    no_watch.append(sys.stdin.readline().strip())    # 정수를 하나씩 입력받아 리스트 no_watch에 추가한다.

ans_num=0
ans_lst = []
all = no_listen + no_watch
counts = Counter(all)
for name, count in counts.items():
    if count > 1:
        ans_num += 1
        ans_lst.append(name)

ans_lst.sort()
print(ans_num)
for name in ans_lst:
    print(name)