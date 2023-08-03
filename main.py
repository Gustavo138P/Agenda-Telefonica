import Biblioteca as b

agenda = []
contador = 0

while True:
  print('\033[1;33m1 = \033[1;36mIncluir Contato\n\033[1;33m2 = \033[1;36mExcluir Contato\n\033[1;33m3 = \033[1;36mListar Contatos\n\033[1;33m4 = \033[1;36mAlterar Contato\033[m\n\033[1;33m5 = \033[1;36mSair do programa\n')
  try:
    opcao = int(input('\033[1;33mDigite a sua opcao:\033[m'))
  except:
    print('\033[1;31mDigite apenas numeros inteiros!!!\033[m\n')
    continue
  if(opcao == 1):
    agenda.append(b.adicionarContatos())
    contador+=1
  elif(opcao == 2):
    if (contador != 0):
      i = 1
      for contato in agenda:
        print(f"\033[1;33mContato {i}\033[m\n\033[1;33mNome: \033[1;36m{contato['nome']}\033[m\n\033[1;33mNumero: \033[1;36m{contato['numero']}\033[m")
        print('\033[1;31m----------------------------------------------\033[m')
        i += 1
      excluir = input('\033[1;33mDigite o nome do contato que vc quer excluir:\033[m ')
      excluir = excluir.title()
      indice = 0
      for contato in agenda:
        if(contato['nome'] == excluir):
          print(f'\n\033[1;33mContato a excluir: \033[1;36m{contato["nome"]}')
          confirmacao = input('\033[1;33mConfirmar(s=sim/n=nao):\033[m ')
          if(confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
            agenda.pop(indice)
            print('\033[1;32mContato excluido com sucesso!!!\033[m\n')
            contador-=1
          else:
            break
        indice += 1
    else:
      print('\033[1;31mLista Vazia, inclua um novo contato!\033[m\n')
  elif(opcao == 3):
    if(contador != 0):
      b.listarContatos(contador, agenda)
    else:
      print('\033[1;31mLista Vazia, inclua um novo contato!\033[m\n')
  elif(opcao == 4):
    if (contador != 0):
      i = 1
      for contato in agenda:
        print(
          f"\033[1;33mContato {i}\033[m\n\033[1;33mNome: \033[1;36m{contato['nome']}\033[m\n\033[1;33mNumero: \033[1;36m{contato['numero']}\033[m")
        print('\033[1;31m----------------------------------------------\033[m')
        i += 1
      alterar = input('\033[1;33mDigite o nome do contato que vc quer alterar:\033[m ')
      alterar = alterar.title()
      indice = 0
      for contato in agenda:
        if (contato['nome'] == alterar):
          print(f'\n\033[1;33mContato a alterar: \033[1;36m{contato["nome"]}')
          confirmacao = input('\033[1;33mConfirmar(s=sim/n=nao):\033[m ')
          if (confirmacao == 's' or confirmacao == 'S' or confirmacao == 'Sim' or confirmacao == 'sim'):
            novoNome = input('\033[1;33mDigite o nome do novo Contato:\033[m ')
            novoNome = novoNome.title()
            contato['nome'] = novoNome
            try:
              contato['numero'] = int(input('\033[1;33mDigite o Numero do novo Contato:\033[m '))
            except:
              print('\033[1;33mNumero do contato Invalido!\033[m')
            else:
              print('\033[1;32mContato alterado com sucesso!!!\033[m\n')
          else:
            break
        indice += 1
    else:
      print('\033[1;31mLista Vazia, inclua um novo contato!\033[m\n')
  elif(opcao == 5):
      print('\033[1;31mPrograma Encerrado!\033[m')
      break
  else:
      print('\033[1;31mOpcao Invalida!\033[m\n')
