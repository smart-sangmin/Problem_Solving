import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[1e9] * (n + 1) for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

solution = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            solution[i] += items[j]
print(max(solution))
