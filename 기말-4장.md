# Exchanges Greedy Algorithm (동전 종류만 명시한 경우)
# 가치가 큰 동전부터 순서대로 나열된 배열 coins
coins = [coin1, coin2, ..., coinN]

def GreedyChange(money, coins):
    change = []
    for coin in coins:
        while money >= coin:    # 동전의 가치가 남은 금액보다 작거나 같을 때
            money -= coin       # 동전의 가치를 남은 금액에서 차감
            change.append(coin) # 동전 추가
    return change

# 가치가 큰 동전부터 순서대로 나열된 배열 coins
# 각 동전의 수량을 추적하는 배열 coinCounts
coins = [coin1, coin2, ..., coinN]
coinCounts = [count1, count2, ..., countN]

def GreedyChange(money, coins, coinCounts):
    change = []
    for i in range(len(coins)):
        coin = coins[i]
        while money >= coin and coinCounts[i] > 0:    # 동전의 가치가 남은 금액보다 작거나 같을 때, 그리고 해당 동전이 아직 남아있을 때
            money -= coin       # 동전의 가치를 남은 금액에서 차감
            coinCounts[i] -= 1  # 동전의 수량을 감소
            change.append(coin) # 동전 추가
    return change

Mininum Spanning Tree
# Kruskal 알고리즘과 Prim 알고리즘으로 구분된다.
# 1 Kruskal 알고리즘
    # STEP 1 그래프의 간선들을 가중치의 오름차순으로 정렬하고, 
    # STEP 2 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
            # 1) 사이클이 발생하지 않으면 최소 신장 트리에 포함시킨다
            # 2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    # STEP 3 모든 간선에 대하여 2번의 과정을 반복한다.
    
# 2. Prim 알고리즘은 특정 정점에서 시작해서 MST에 포함된 정점들과 연결된 간선 중에서 가장 가벼운 간선을 선택해 MST를 만듭니다.

# 다시 말해서, Kruskal 알고리즘은 전체 간선을 대상으로 작동하고, Prim 알고리즘은 MST에 연결된 간선들만을 대상으로 작동합니다.

function Kruskal(G):
    // 각각의 정점들로 구성된 부분집합을 생성합니다.
    for each vertex v in G.V:
        MAKE_SET(v)

    // 결과를 담을 리스트를 초기화합니다.
    A = empty list

    // 가중치에 따라 간선들을 오름차순으로 정렬합니다.
    sort the edges of G.E into non-decreasing order by weight

    // 각각의 간선에 대하여 순회합니다.
    for each edge (u, v) in G.E:
        // u와 v가 다른 집합에 속해 있다면
        if FIND_SET(u) != FIND_SET(v):      // 사이클 생성 방지
            // 결과 리스트에 (u, v)를 추가합니다.
            A = A ∪ {(u, v)}
            // u와 v가 속한 집합을 합칩니다.
            UNION(u, v)

    // 최소 신장 트리를 구성하는 간선들을 반환합니다.
    return A

function Prim(graph, startNode):
    // 각 노드를 가중치를 INF로 초기화하고 부모 노드를 None으로 설정
    for each node in graph:
        node.minimumCost = INF
        node.parent = None

    // 시작 노드의 가중치를 0으로 설정
    startNode.minimumCost = 0

    // 우선순위 큐 PriorityQ를 graph의 노드들로 초기화
    PriorityQ = list(graph.nodes)

    // PriorityQ가 비어있지 않는 동안 다음을 반복
    while PriorityQ is not empty:
        // PriorityQ에서 가중치가 가장 작은 노드 currentNode를 선택하고 제거
        currentNode = selectNodeWithMinimumCost(PriorityQ)
        PriorityQ.remove(currentNode)

        // currentNode와 인접한 모든 노드에 대하여
        for node in currentNode.adjacentNodes:
            // node가 PriorityQ에 있고, 가중치가 node의 현재 가중치보다 작다면
            if node in PriorityQ and weight(currentNode, node) < node.minimumCost:
                // node의 부모를 currentNode로 설정하고 가중치를 업데이트
                node.parent = currentNode
                node.minimumCost = weight(currentNode, node)
                
    // 부모 노드와 가중치 정보를 반환
    return all nodes with their parent and minimumCost


// 다익스트라 알고리즘은 시작 노드에서 다른 모든 노드로 가는 최단 경로를 찾는 알고리즘입니다. 그 결과는 각 노드까지의 최단 경로와 그 거리가 됩니다. 여기서 중요한 것은 '최단 경로'입니다.
function Dijkstra(graph, startNode):
    // 모든 노드의 거리를 INF로 초기화하고 부모 노드를 None으로 설정
    for each node in graph:
        node.distance = INF
        node.parent = None

    // 시작 노드의 거리를 0으로 설정
    startNode.distance = 0

    // 우선순위 큐 PriorityQ를 graph의 노드들로 초기화
    PriorityQ = list(graph.nodes)

    // PriorityQ가 비어있지 않는 동안 다음을 반복
    while PriorityQ is not empty:
        // PriorityQ에서 거리가 가장 짧은 노드 currentNode를 선택하고 제거
        currentNode = selectNodeWithMinimumDistance(PriorityQ)
        PriorityQ.remove(currentNode)

        // currentNode와 인접한 모든 노드에 대하여
        for node in currentNode.adjacentNodes:
            // node가 PriorityQ에 있고, 거리가 node의 현재 거리보다 작다면
            if node in PriorityQ and weight(currentNode, node) + currentNode.distance < node.distance:
                // node의 부모를 currentNode로 설정하고 거리를 업데이트
                node.parent = currentNode
                node.distance = weight(currentNode, node) + currentNode.distance

    // 부모 노드와 거리 정보를 반환
    return all nodes with their parent and distance

// 분할 가능한 냅색문제
function FractionalKnapsack(items, capacity):
    // items를 value/weight 비율이 높은 순으로 정렬
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    totalValue = 0
    for item in items:
        if capacity == 0:
            return totalValue
        
        // 아이템을 배낭에 넣을 수 있는 만큼의 양 a를 계산
        a = min(item.weight, capacity)
        totalValue += a * (item.value / item.weight)
        
        // 배낭의 남은 용량을 업데이트
        capacity -= a
    return totalValue
