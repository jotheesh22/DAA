V = 3
G = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]
def prim_mst(graph):
    selected = [False] * V
    selected[0] = True
    edges = 0
    print("Edge : Weight")
    while edges < V - 1:
        m = 999999
        x = y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if m > graph[i][j]:
                            m = graph[i][j]
                            x, y = i, j
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
        edges += 1
prim_mst(G)
