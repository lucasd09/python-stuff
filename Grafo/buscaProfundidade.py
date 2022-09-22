def buscaProfundidade(grafo, v):
    visitados = set()

    def dfs_recursiva(grafo, v):
        visitados.add(v)
        for adj in grafo[v]:
            if adj not in visitados:
                dfs_recursiva(grafo, adj)

    dfs_recursiva(grafo, v)

    if len(visitados) == len(grafo):
      print('Este grafo é Conexo')
    else:
      print('Este grafo é Desconexo')