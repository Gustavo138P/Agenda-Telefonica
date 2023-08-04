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
    contador = b.excluirContato(contador, agenda)
  elif(opcao == 3):
    b.listarContatos(contador, agenda)
  elif(opcao == 4):
    b.alterarContato(contador, agenda)
  elif(opcao == 5):
      print('\033[1;31mPrograma Encerrado!\033[m')
      break
  else:
      print('\033[1;31mOpcao Invalida!\033[m\n')
