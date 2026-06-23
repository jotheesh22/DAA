V = 4  
edges = [
    (0, 1, 2),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 5)
]
parent = list(range(V))
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
def union(i, j):
    a, b = find(i), find(j)
    parent[a] = b
edges.sort(key=lambda x: x[2])
print("Edge : Weight")
count = 0
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        print(f"{u} - {v} : {w}")
        count += 1
        if count == V - 1:
            break
