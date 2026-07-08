import numpy as np

def CreateMatrix(n, density):
    matrix = np.round(np.random.rand(n, n),2)
    matrix = (matrix > (1 - density)).astype(int)
    matrix = np.triu(matrix) + np.triu(matrix, 1).T
    np.fill_diagonal(matrix, 0)
    return matrix

n = int(input("Введите количество вершин: "))
density = int(input("Введите плотность графа в  % (вероятность наличия ребра): "))
GraphMatrix=CreateMatrix(n, density/100)
print(GraphMatrix)
np.savetxt('RandomAdjacencyMatrix.txt', GraphMatrix, fmt='%d')