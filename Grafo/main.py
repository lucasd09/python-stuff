from menu import *
from createAresta import CreateArestas
from createGrafo import CreateGrafo
from createVertice import CreateVertices
from printGrafo import PrintGrafo
from validaGrafo import ValidaGrafo

print("Construção e Validação de grafos em Python: \n")
print('Como Funciona:')
print('Primeiro, insira um grafo para ser validado')
print('Depois, você pode validar de 2 formas: \n 1. Busca em profundidade \n 2. Busca em largura \n 3. Verificar se há ciclos \n')

print("CONSTRUINDO O GRAFO\n")

vertices = CreateVertices()
arestas = CreateArestas(vertices)
grafo = CreateGrafo(vertices, arestas)
metodo = 'profundidade'

while True:
  opc = Menu()

  if opc == 1:
    vertices = CreateVertices()
    arestas = CreateArestas(vertices)
    grafo = CreateGrafo(vertices, arestas)
  
  if opc == 2:
    while True:
      opc = MenuValidar()

      if opc == 1:
        pass

      if opc == 2:
        pass

      if opc == 3:
        break

  if opc == 3:
    pass

  if opc == 4:
    print('Fim do algoritmo')
    break



print("\nGrafo construído:")
PrintGrafo(grafo)
ValidaGrafo(grafo, vertices[0], metodo)
