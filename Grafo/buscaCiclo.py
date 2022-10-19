def BuscaCiclo(grafo, v):
    possibleV = [v]
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
    cont = 0
    ciclo = False
    for i in possibleV:
        if cont == 1:
            cont += 1
            continue
        if v in grafo[i]:
            ciclo = True
            break
        cont += 1
    if ciclo == True:
        print('Há ciclos')
    else:
        print('Não há ciclos')