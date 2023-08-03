import Biblioteca as b

agenda = []
contador = 0

while True:
  print('1 = Incluir Contato\n2 = Excluir Contato\n3 = Listar Contatos\n4 = Sair do Programa\n')
  try:
    opcao = int(input('Digite a sua opcao:'))
  except:
    print('\033[1;31mDigite apenas numeros inteiros!!!\033[m')
    continue
  if(opcao == 1):
    agenda.append(b.adicionarContatos())
    contador+=1
  elif(opcao == 2):
    if (contador != 0):
      i = 1
      for contato in agenda:
        print(f"Contato {i}\nNome: {contato['nome']}\nNumero: {contato['numero']}")
        print('----------------------------------------------')
        i += 1
      excluir = input('Digite o nome do contato que vc quer excluir: ')
      excluir = excluir.title()
      indice = 0
      for contato in agenda:
        if(contato['nome'] == excluir):
          print(f'\nContato a excluir: {contato["nome"]}')
          confirmacao = input('Confirmar(s=sim/n=nao): ')
          if(confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
            agenda.pop(indice)
            print('\033[1;32mContato excluido com sucesso!!!\033[m')
            contador-=1
          else:
            break
        indice += 1
    else:
      print('\033[1;33mLista Vazia, inclua um novo contato!\033[m')
  elif(opcao == 3):
    if(contador != 0):
      b.listarContatos(contador, agenda)
    else:
      print('\033[1;33mLista Vazia, inclua um novo contato!\033[m')
  elif(opcao == 4):
      print('\033[1;31mPrograma Encerrado!\033[m')
      break
  else:
      print('\033[1;33mOpcao Invalida!\033[m')
