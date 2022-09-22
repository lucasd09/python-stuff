from validaAresta import ValidaAresta

def CreateArestas(vertices):
  arestas = []
  print('insira X para sair:')
  while True:
    
    a = input("Pares de arestas(EX: V1, V2):").upper().split(',')
    if ValidaAresta(a, vertices):
      arestas.append(a)
    else:
      print("Valor de aresta invalido")
      break
  return arestas