def CreateGrafo(vertices, arestas):
  grafo = {}
  for v in vertices:
    grafo[v] = {}
    arestasGrafo = []
    for a in arestas:
      if v in a:
        vert = [x for x in a if x != v and x not in arestasGrafo]
        if len(vert) > 0:
          arestasGrafo.append(vert[0])
    grafo[v] = arestasGrafo
  
  return grafo