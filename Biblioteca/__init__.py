def adicionarContatos():
    atual = dict()
    nome = input('\033[1;33mDigite o nome do novo Contato:\033[m ')
    nome = nome.title()
    atual['nome'] = nome
    try:
        atual['numero'] = int(input('\033[1;33mDigite o Numero do novo Contato:\033[m '))
    except:
        print('\033[1;33mNumero do contato Invalido!\033[m')
        exit(0)
    else:
        return atual

def listarContatos(contador, agenda):
    if (contador != 0):
        i = 1
        for contato in agenda:
            print(f"\033[1;33mContato {i}\033[m\n\033[1;33mNome: \033[1;36m{contato['nome']}\033[m\n\033[1;33mNumero: \033[1;36m{contato['numero']}\033[m")
            print('\033[1;31m----------------------------------------------\033[m')
            i += 1
    else:
      print('\033[1;31mLista Vazia, inclua um novo contato!\033[m\n')

def excluirContato(contador, agenda):
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
            return contador
          else:
            return contador
        indice += 1
    else:
      print('\033[1;31mLista Vazia, inclua um novo contato!\033[m\n')

def alterarContato(contador, agenda):
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