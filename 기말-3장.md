이항 계수

procedure BinomialCoefficient(n, k):
  // n * k 크기의 2차원 배열 dp를 초기화합니다.
  Initialize an array dp[0...n][0...k] 

  // i를 0부터 n까지 순회합니다.
  for i from 0 to n:
    // j를 0부터 i와 k 중 작은 수까지 순회합니다.
    for j from 0 to min(i, k):
      // j가 0이거나 i와 같은 경우, 이항계수의 값은 1이 됩니다.
      if j == 0 or j == i: 
        dp[i][j] = 1 
      // 그 외의 경우, 이항계수의 값을 재귀적인 방식으로 계산합니다.
      else: 
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

  // n개의 원소 중 k개를 선택하는 경우의 수를 반환합니다.
  return dp[n][k]

플로이드 알고리즘
procedure floydWarshall(graph):
  // graph[i][j]는 i에서 j까지의 시작 비용을 의미합니다. 만약 경로가 없다면 무한대(INF)로 설정합니다.
  
  // 각 노드를 모든 다른 노드에 대한 경유지로 설정합니다.
  for k from 1 to number of vertices:
    // 해당 경유지를 통해 지나가는 모든 노드 쌍에 대해
    for i from 1 to number of vertices:
      for j from 1 to number of vertices:
        // 만약 정점 i에서 k를 거쳐 j로 가는 거리가 직접 가는 것보다 짧다면 업데이트 합니다.
        if graph[i][k] + graph[k][j] < graph[i][j]:
          graph[i][j] = graph[i][k] + graph[k][j]
  
  // 모든 노드 쌍의 최단 거리를 갖는 그래프를 반환합니다.
  return graph


// 이 함수는 최단 경로의 길이만을 계산합니다. 경유지에 대한 정보는 무시하고, 각 노드 쌍 (i, j) 사이의 최단 경로의 길이만을 계산
void floyd (int n, const number W[][], number D[][])
{
	index i, j, k;
	D = W;
	for (k = 1; k<=n; k++)
		for (i=1; i<=n; i++)
			for(j=1;j<=n;j++)
				D[i][j] = minimum(D[i][j], D[i][k]+D[k][j]);
}

// 이 함수는 최단 경로의 길이뿐만 아니라, 그 경로를 구성하는 노드에 대한 정보까지 함께 계산합니다. 각 노드 쌍 (i, j)의 최단 경로를 구성하는 중간 경유지를 P[i][j]에 저장합니다. 이를 통해 경로 자체를 추적할 수 있습니다.
void floyd2(int n, const number W[][], D[][], P[][])
{
	index n, i, j, k;
	for (i = 1; i<=n; i++)
		for (j=1; j<=n; j++)
			P[i][j] = 0;
	D = W;
	for (k=1; k<=n; k++)
		for(i=1; i<=n; i++)
			for(j=1; j<=n; j++)
				if(D[i][k] + D[k][j] < D[i][j])
				{
					P[i][j] = k;
					D[i][j] = D[i][k]+D[k][j];
				}
}

//Chained Matrix Multiplication 최소 곱셈 횟수, 최적의 곱셈 순서를 출력
function PrintOptimalParens(s, i, j)
    if i == j                    	// 만약 i와 j가 같으면 하나의 행렬만 출력
        print "A" + i
    else                         	// 그렇지 않으면 두 부분으로 분할
        print "("                	// 분할의 시작을 "("로 표시
        PrintOptimalParens(s, i, s[i][j])   // 왼쪽 부분을 재귀적으로 출력
        PrintOptimalParens(s, s[i][j] + 1, j)  // 오른쪽 부분을 재귀적으로 출력
        print ")"                	// 분할의 끝을 ")"로 표시


function MatrixChainOrder(p, n)
    for i from 1 to n           		// 모든 i에 대해 주 대각선에 0 설정
        m[i][i] = 0
    for chain_length from 2 to n 	// 체인의 길이별로 계산 시작
        for i from 1 to (n - chain_length + 1) // 체인의 시작점 설정
            j = i + chain_length - 1    	// 체인의 끝점 설정
            m[i][j] = Infinity   		// i부터 j까지의 최소 곱셈 횟수를 무한대로 초기화
            for k from i to (j - 1)  	// 가능한 모든 분할 지점에 대해 최소값 계산
                cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]  // 분할 지점 k에서의 곱셈 횟수 계산
                if cost < m[i][j]   		// 현재의 최소값보다 cost가 작으면 업데이트
                    m[i][j] = cost
                    s[i][j] = k  		// 최적의 분할 지점 저장
    return m and s   		// 최소 곱셈 횟수를 저장하는 m과 최적 분할 지점을 저장하는 s 반환

# p와 n은 입력값
m, s = MatrixChainOrder(p, n)
PrintOptimalParens(s, 1, n) 		// 최적의 곱셈 순서를 출력


# Traveling Salesman Problem 수도 코드
function tsp(DP, last, visited)
    // 모든 도시를 방문한 경우
    if all cities are visited:
        return DP[last][0] if DP[last][0] > 0 else INF

    // 이미 계산된 경우, DP[last][visited]는 "마지막으로 방문한 도시가 last이고, 현재까지 방문한 도시들의 집합이 visited일 때, 현재 위치에서 출발점으로 돌아가는데 필요한 최소 비용
    if DP[last][visited] != 0:
        return DP[last][visited]

    DP[last][visited] = INF                      //  우선 현재 상태(마지막으로 방문한 도시와 지금까지 방문한 도시들의 집합)에 대해 최소 비용을 INF로 초기화
    for i in range(0, n):
        // 아직 방문하지 않은 도시라면
        if visited[i] == false:                                 // 아직 방문하지 않은 도시 i에 대해 연산을 수행
            visited[i] = true                                   // 도시 i를 방문했다고 표시
            temp = tsp(DP, i, visited) + dist[last][i]
            // 다음 도시를 i로 설정하고, 그 도시에서의 최소 여행 비용(tsp(DP, i, visited))과 현재 도시에서 도시 i까지의 거리(dist[last][i])를 더한 값을 temp에 저장합니다. 이 temp 값은 현재 도시에서 도시 i를 거쳐서 모든 도시를 순회하는데 필요한 비용을 나타냅니다.

            DP[last][visited] = min(DP[last][visited], temp)
            // 이제 DP[last][visited]에는 현재 도시에서 도시 i를 거치는 경우를 포함하여 모든 도시를 순회하는데 필요한 최소 비용이 저장됩니다. 여기서 도시 i는 아직 방문하지 않은 모든 도시를 대상으로 합니다
            visited[i] = false

    return DP[last][visited]


# 0/1 Knapsack problem
function knapsack(items, capacity):
    // n은 아이템의 수
    n = length(items)

    // DP 테이블 생성. (n+1) x (capacity+1) 크기의 2차원 배열
    DP = array of zeros with dimensions (n+1) x (capacity+1)

    // 각 아이템에 대해 DP 테이블을 채워나감
    for i from 1 to n:
        for w from 0 to capacity:
            if items[i-1].weight <= w:
                DP[i][w] = max(DP[i-1][w], items[i-1].value + DP[i-1][w - items[i-1].weight])
            else:
                DP[i][w] = DP[i-1][w]

    // DP 테이블의 마지막 값이 최대 가치
    return DP[n][capacity]
