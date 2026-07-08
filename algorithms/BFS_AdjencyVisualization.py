import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def BFS_Visualization(graph, start_node):
    visited = set()
    queue = deque([start_node])
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(16, 9))
    paused = False

    def on_key(event):
        nonlocal paused
        if event.key == ' ':
            paused = not paused
            if paused:
                print("ПАУЗА. Нажмите ПРОБЕЛ для продолжения...")
            else:
                print("ПРОДОЛЖЕНИЕ...")
        elif event.key == 'escape':
            plt.close()
            sys.exit(0)
            return

    while len(queue)>=0:

        plt.gcf().canvas.mpl_connect('key_press_event', on_key)

        plt.clf()

        # Нарисовать граф
        node_colors = ['#00CC00' if node in visited else 'orange' if node in queue else 'lightblue' for node in graph.nodes()]
        nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=400, font_size=14)

        queue_text = f"Очередь: {list(queue)}"
        plt.text(0.05, 0.95, queue_text, horizontalalignment='left', verticalalignment='top',
                 transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        visited_text = f"Посещённые: {list(visited)}"
        plt.text(0.05, 0.90, visited_text, horizontalalignment='left', verticalalignment='top',
                 transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

        status = "ПАУЗА" if paused else "ВЫПОЛНЕНИЕ"
        plt.text(0.05, 0.05, f"Статус: {status} (ПРОБЕЛ - пауза/продолжить)", horizontalalignment='left', verticalalignment='bottom', transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='lightgray', alpha=0.5))

        while paused:
            plt.pause(0.1)

        if len(queue)==0:
            break
        else:
            node = queue.popleft()
        if node not in visited:
            visited.add(node)
            new_neighbors=[]
            for neighbor in graph.neighbors(node):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    new_neighbors.append(neighbor)

        new_edges = [(node, neighbor) for neighbor in new_neighbors]
        nx.draw_networkx_edges(graph, pos, edgelist=new_edges,
                               width=7, alpha=0.75, edge_color='green')
        plt.draw()
        plt.pause(pause)
    plt.show()

#Загрузка графа из файла
loaded_matrix = np.loadtxt('RandomAdjacencyMatrix.txt', dtype=int)
print("Загруженная матрица смежности: ")
print(loaded_matrix)

def GraphFromMatrix(Matrix):
    G = nx.Graph()
    n = Matrix.shape[0]

    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(i + 1, n):
            if Matrix[i, j] > 0:
                G.add_edge(i, j, weight=Matrix[i, j])
    return G

Graph = GraphFromMatrix(loaded_matrix)
pause=float(input("\nВведите время паузы между шагами (в сек.): "))
BFS_Visualization(Graph, 0)


