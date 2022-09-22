def CreateVertices():
  n = int(input('Quantidade de vertices:'))
  vertices = []
  i = 0
  for i in range(n):
    vertices.append(f'V{i+1}')

  return vertices