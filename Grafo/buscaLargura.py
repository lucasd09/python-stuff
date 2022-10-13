def buscaLargura(grafo,v):
    print('Keys : ',grafo.keys())
    print('Values : ',grafo.values())
    possibleV = [v]
    print(possibleV[0])
    for i in grafo:
        if i == possibleV[0]:
            visitados = [v,grafo[v][0]]
        
    while True:
        for i in possibleV:
            if grafo[i] not in possibleV:
                for j in grafo[i]:
                    if j not in possibleV:
                        visitados.append(j)
                        possibleV.append(j)
                    continue
        break
    if len(possibleV) != len(grafo):
        print('Grafo desconexo')
    else:
        print('Grafo conexo')



    return visitados