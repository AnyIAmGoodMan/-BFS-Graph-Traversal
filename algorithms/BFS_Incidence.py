file = open('RandomIncidenceMatrix.txt')
tabl = [list(map(int, strok.split())) for strok in file]

connections_all = []
connections = []
vers = []
result = []
to_watch_vers = []
now_lvl = []
zam = []
distance = 0
visit = 0


n = max(max(a,b) for a,b in tabl)          
connections_all = [[] for x in range(n)]  

for a, b in tabl:
    connections_all[a-1].append(b)   

for i in range(len(connections_all)):
    vers.append(i+1)
    result.append(0)

start_ver = int(input("Начальная вершина:")) #вводим начальную вершину
now_ver = start_ver
now_lvl.append(now_ver)
to_watch_vers.append(now_ver)

while len(vers) != 0: #сам алгоритм
    distance +=1
    while (len(now_lvl)) != 0:
        now_ver = now_lvl[0]
        print("Рассматриваемая вершина:", now_ver)
        for i in range(len(connections_all[now_ver-1])):
            if (connections_all[now_ver-1][i] in vers) and (connections_all[now_ver-1][i] not in zam) and (connections_all[now_ver-1][i] not in to_watch_vers):
                zam.append(connections_all[now_ver-1][i])
                to_watch_vers.append(connections_all[now_ver-1][i])
                result[connections_all[now_ver-1][i]-1] = distance
        visit += 1
        vers = [x for x in vers if x != now_ver]
        now_lvl = [x for x in now_lvl if x != now_ver]
        to_watch_vers.pop(0)
        print("Произведено операций:", visit," Текущая дистанция:", distance-1)
        print("Очередь:", to_watch_vers)
        print(" ")
    now_lvl = zam
    zam = []
    if len(now_lvl) == 0: #если нет связи
        for i in range(len(result)):
            if (i+1 != start_ver) and (result[i] == 0):
                result[i] = "нет связи"
        break
        

for i in range(len(result)):
    print("Расстояние до вершины", i+1, ":", result[i])
