def ValidaAresta(aresta, vertices):
  for a in aresta:
    if a not in vertices:
      return False
  return True    