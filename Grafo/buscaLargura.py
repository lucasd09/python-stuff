def buscaLargura(grafo, vertice_fonte):
    visitados, fila = set(), [vertice_fonte]
    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)
    return visitados