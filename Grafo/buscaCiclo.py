def BuscaCiclo(grafo, vertice_fonte):
        visitados = set()
        restantes = [vertice_fonte]

        while restantes:
            atual = restantes.pop()
            visitados.add(atual)

            for vizinho in grafo[atual]:
                if vizinho in visitados:
                    return True

                restantes.append(vizinho)

        return False