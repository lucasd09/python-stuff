from buscaCiclo import BuscaCiclo
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

while True:
  opc = Menu()

  if opc ==  1:
    vertices = CreateVertices()
    arestas = CreateArestas(vertices)
    grafo = CreateGrafo(vertices, arestas)

  if opc ==  2:
    print('\n')
    PrintGrafo(grafo)
    print('\n')

  if opc ==  3:
    metodo = MenuValidar()

    if metodo == 'profundidade' or 'largura':
      print('\n')
      PrintGrafo(grafo)
      ValidaGrafo(grafo, vertices[0], metodo)
      print('\n')
        
  if opc ==  4:
    print('\n')
    PrintGrafo(grafo)
    if BuscaCiclo(grafo, vertices[0]):
      print('Há ciclos nesse grafo')
    else:
      print('Não há ciclos nesse grafo')
    print('\n')

  if opc ==  5:
    print('Fim do algoritmo')
    break


#print("\nGrafo construído:")
#PrintGrafo(grafo)
#ValidaGrafo(grafo, vertices[0], metodo)
