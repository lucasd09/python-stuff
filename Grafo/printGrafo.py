def PrintGrafo(grafo):
  vertices = list(grafo.keys())
  for v in vertices:
    print(f'{v} => {grafo[v]}')