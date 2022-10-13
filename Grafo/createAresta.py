from validaAresta import ValidaAresta

def CreateArestas(vertices):
  arestas = []
  print('insira Vazio para sair:')
  while True:
    
    a = input("Pares de arestas(EX: V1,V2):").upper().split(',')
    if ValidaAresta(a, vertices):
      arestas.append(a)
    else:
      break
  return arestas