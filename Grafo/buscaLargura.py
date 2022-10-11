def buscaLargura(grafo):
    visitados, filaB = set(), list(grafo.values())
    print('Fila : ',filaB)
    fila = []
    for i in filaB:
        if i != []:
            fila.append(i[0])
    
    while len(fila) > 0:
        v = fila.pop(0)
        if v not in visitados:
            visitados.add(v)
            fila.extend((grafo[v]).remove(v))
            
    
    print(len(visitados))
    print(len(grafo))
    return visitados