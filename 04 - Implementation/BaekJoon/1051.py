'''
n, m 입력을 받습니다.
a 리스트 내에 직사각형 값을 입력 받습니다.
행과 열 중에 작은 값을 k에 넣습니다(그게 정사각형의 최대 길이니까)
기본값을 1로 설정했으니, 최소 길이가 2인것부터 최대 길이는 k인것까지 반복하면서 i, j 크기를 늘려가면서 확인합니다.
만약 같은 값이 발견되면 max로 비교하여 ans에 넣습니다.
'''
#!/usr/bin/env python3
n, m = map(int, input().split())
if n < 1 or n > 50 or m < 1 or m > 50:
    print("N과 M은 1 이상 50 이하의 자연수여야 합니다.")
else:
    # 입력으로 주어진 직사각형을 2차원 리스트로 저장합니다.
    a = [list(input()) for _ in range(n)]
    k = min(n,m)
    ans = 1
    for l in range(2,k+1):
        for i in range(n-l+1):
            for j in range(m-l+1):
                if a[i][j] == a[i+l-1][j] == a[i][j+l-1] == a[i+l-1][j+l-1]:
                    ans = max(ans,l)
    print(ans**2)