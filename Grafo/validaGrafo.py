from buscaLargura import buscaLargura
from buscaProfundidade import buscaProfundidade

def ValidaGrafo(grafo, v, metodo):
  if metodo == 'profundidade':
    buscaProfundidade(grafo, v)

  if metodo == 'largura':
    buscaLargura(grafo, v)