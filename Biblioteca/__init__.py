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

def listarContatos(contador,agenda):
    if (contador != 0):
        i = 1
        for contato in agenda:
            print(f"\033[1;33mContato {i}\033[m\n\033[1;33mNome: \033[1;36m{contato['nome']}\033[m\n\033[1;33mNumero: \033[1;36m{contato['numero']}\033[m")
            print('\033[1;31m----------------------------------------------\033[m')
            i += 1