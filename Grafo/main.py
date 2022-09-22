from createAresta import CreateArestas
from createGrafo import CreateGrafo
from createVertice import CreateVertices
from printGrafo import PrintGrafo
from validaGrafo import ValidaGrafo

print("CONSTRUINDO O GRAFO\n")

vertices = CreateVertices()
arestas = CreateArestas(vertices)
grafo = CreateGrafo(vertices, arestas)

print("\nGrafo construído:")
PrintGrafo(grafo)
ValidaGrafo(grafo, vertices[0])
