def Menu():
  print('----- GRAFOS ----- \n')
  print('1. Alterar Grafo')
  print('2. Mostrar Grafo')
  print('3. Validar Grafo')
  print('4. Verificar se há ciclo no Grafo')
  print('5. Sair')
  return int(input('Escolha -> '))

def MenuValidar():
  print('----- VERIFICAÇÃO ----- \n')
  print('1. Verificar usando o algoritmo de Busca em Profundidade')
  print('2. Verificar usando o algoritmo de Busca em Largura')
  print('3. Voltar')
  opc = int(input('Escolha -> '))

  match opc:
    case 1:
      return 'profundidade'
    case 2:
      return 'largura'
    case 3:
      return 

