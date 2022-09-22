def ValidaGrafo(grafo, v):
    visitados = set()

    def buscaRecursiva(grafo, v):
        visitados.add(v)
        for adj in grafo[v]:
            if adj not in visitados:
                buscaRecursiva(grafo, adj)
    
    buscaRecursiva(grafo, v)
    
    if len(visitados) == len(grafo):
      print('Este grafo é Conexo')
    else:
      print('Este grafo é Desconexo')
    