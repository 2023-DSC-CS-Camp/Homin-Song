# 입력값 전처리
nodes_num, edges_num, start_point = map(int, input().split())

# 그래프에 노드 및 간선 정보 생성
# (1) 그래프 및 노드 초기화
graph = {}
for node in range(nodes_num):
    graph[node + 1] = []
# (2) 노드별 간선 정보 생성
for edge in range(edges_num):
    first, second = map(int, input().split())
    for e in graph.keys():
        if e == first:
            graph[second].append(first)
        elif e == second:
            graph[first].append(second)

# dfs 알고리즘
def dfs(graph, start_point):
    visited = set()
    stack = [start_point]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            stack.extend(sorted(list(set(graph[vertex]) - visited), reverse=True))
            
# bfs 알고리즘
def bfs(graph, start_point):
    visited = set()
    queue = [start_point]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend(sorted(list(set(graph[vertex]) - visited)))

if __name__ == "__main__":
    dfs(graph, start_point)
    print()
    bfs(graph, start_point)