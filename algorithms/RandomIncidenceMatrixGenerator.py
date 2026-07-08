import random

n = int(input("Число вершин: "))
edges = []
edges_1 = []
for i in range(1, n + 1):
    for j in range(i+1, n + 1):
        if random.random() <= 0.5:
            edges.append((i,j))
        
for x,y in edges:
    edges_1.append((x,y))
    edges_1.append((y,x))

edges_1.sort()

with open("RandomIncidenceMatrix.txt", "w", encoding="utf-8") as f:
    for x,y in edges_1:
        print(x,y, file=f)
