# 벨만포드 알고리즘
# 음수 간선이 포함된 상황에서의 최단거리 문제
# 시간복잡도 = 정점의개수 * 간선의 개수 => O(VE)
# 다익스트라보다 느림
# -------------------------------
# 1. 출발 노드를 설정한다.
# 2. 최단거리 테이블을 초기화한다.
# 3. 다음의 과정을 N - 1번 반복한다.
# 3-1. 전체 간선 E개를 하나씩 확인한다.
# 3-2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블을 갱신한다.
# 만약 음수 간성 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행한다.
# - 이때 최단거리 테이블이 갱신된다면 음수간선 순환이 존재하는 것이다. 

import sys

def bellManFord(start):
    # 시작 노드 초기화
    distance[start] = 0
    # 전체 N번의 라운드(round) 진행
    for i in range(N):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(M):
            now_node = edge[j][0]
            next_node = edge[j][1]
            cost = edge[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[now_node] != int(1e9) and distance[next_node] > distance[now_node] + cost:
                distance[next_node] = distance[now_node] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N - 1:
                    return True
    return False

N, M = map(int, sys.stdin.readline().split())
edge = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edge.append([A, B, C])
distance = [int(1e9)] * (N +1)

negative_cycle = bellManFord(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단거리 출력
    for i in range(2, N + 1):
        # 도달할 수 없는 경우, -1을 출력
        if distance[i] == int(1e9):
            print("-1")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])