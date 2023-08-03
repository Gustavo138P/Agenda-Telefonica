def adicionarContatos():
    atual = dict()
    nome = input('Digite o nome do novo Contato: ')
    nome = nome.title()
    atual['nome'] = nome
    try:
        atual['numero'] = int(input('Digite o Numero do novo Contato: '))
    except:
        print('\033[1;33mNumero do contato Invalido!\033[m')
        exit(0)
    else:
        return atual

def listarContatos(contador,agenda):
    if (contador != 0):
        i = 1
        for contato in agenda:
            print(f"Contato {i}\nNome: {contato['nome']}\nNumero: {contato['numero']}")
            print('----------------------------------------------')
            i += 1