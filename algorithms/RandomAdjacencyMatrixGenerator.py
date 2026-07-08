import random

n = int(input("Число вершин: "))
matrix = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(i+1, n): 
        if random.random() <= 0.7:
            matrix[i][j] = matrix[j][i] = 1
    print(matrix[i])

with open("RandomAdjacencyMatrix.txt", "w", encoding="utf-8") as f:
    for row in matrix:
        print(*row, file=f)
