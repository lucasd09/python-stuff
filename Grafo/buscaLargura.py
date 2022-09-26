def buscaLargura(grafo):
    visitados, fila = set(), list(grafo.keys())
    
    while len(fila) > 0:
        v = fila.pop(0)

        if v not in visitados:
            visitados.add(v)
            fila.extend(list(grafo[v]).remove(list(visitados)))
    
    print(len(visitados))
    print(len(grafo))
    return visitados