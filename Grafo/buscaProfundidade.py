def dfs_recursiva(grafo, vertice, visitados):
    visitados.add(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs_recursiva(grafo, vizinho, visitados)

def dfs(grafo, vertice):
    visitados = set()
    dfs_recursiva(grafo, vertice, visitados)