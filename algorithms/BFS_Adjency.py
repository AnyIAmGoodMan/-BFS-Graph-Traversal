from collections import deque

file = open('RandomAdjacencyMatrix.txt')
tabl = [list(map(int, strok.split())) for strok in file]

connections = []
connections_all = []
visit = 0
dist = [-1] * len(tabl)
visited = [False] * len(tabl)

for a in range(len(tabl)):
    for b in range(len(tabl[a])):
        if tabl[a][b] !=0:
            connections.append(b+1)
    connections_all.append(connections)
    connections = []

start_ver = int(input("Начальная вершина: "))
dist[start_ver - 1] = 0
visited[start_ver - 1] = True
q = deque([start_ver])

while q:
    v = q.popleft()
    visit += 1

    print("Рассматриваемая вершина:", v)
    print("Произведено операций:", visit, "Текущая дистанция:", dist[v - 1])
    for u in connections_all[v - 1]:
        if not visited[u - 1]:
            visited[u - 1] = True
            dist[u - 1] = dist[v - 1] + 1
            q.append(u)
    print("Очередь:", list(q))
    print()

for i in range(len(tabl)):
    if dist[i] == -1:
        print("Расстояние до вершины", i + 1, ":", "нет связи")
    else:
        print("Расстояние до вершины", i + 1, ":", dist[i])
