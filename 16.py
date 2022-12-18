import matplotlib.pyplot as plt
import networkx as nx

with open('input/16.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def is_deletable(valve):
    return rates[valve] == 0 and valve != start


start = None
graph, graph2 = {}, {}
rates = {}
for line in lines:
    line = line.replace('Valve ', '').split(';')
    name, rate = line[0].split(' has flow rate=')
    values = line[1].split(', ')
    values[0] = values[0][-2:]
    graph[name] = [(x, 1) for x in values]
    rates[name] = int(rate)
    if start is None:
        start = name

for key in graph:
    if is_deletable(key):
        for i, (value1, weight1) in enumerate(graph[key]):
            for j, (value2, weight2) in enumerate(graph[key]):
                if value1 != value2:
                    graph[value1].append((value2, (weight1 + weight2)))

for key in list(graph):
    if not is_deletable(key):
        for i, (value, weight) in enumerate(graph[key]):
            if not is_deletable(value):
                graph2.setdefault(key, {}).setdefault(value, weight)
                graph2[key][value] = min(graph2[key][value], weight)

print(graph2)
print(rates)

g = nx.Graph()
for k in graph2:
    for v in graph2[k]:
        g.add_edge(v, k, weight=graph2[k][v])
nx.draw_networkx(g)
plt.show()

###

