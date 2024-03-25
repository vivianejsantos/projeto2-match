
# cadastro de livros

#consultar livros
#------Inicio das variaveis globais-----
lista_livro=[]
codigo_livro=0



#------fim das variaveis globais-----

#------INICIO DE CADASTRAR_LIVROS()------
def cadastrar_livro(codigo):

    print('----Menu de Cadastrar livros----')
    print('\n código do livro: {}'.format(codigo))
    titulo=input('Entre com Titulo do livro: \n')
    autor=input('Entre com autor do livro: \n')
    while True:
        try:
            numeroDeExemplares=int(input('Entre com numero de exemplares disponíveis: \n'))
            if(numeroDeExemplares<=0):      #verifica se o numero de exemplares é maior que 0

                print('ATENÇÃO!!! Cadastre livro com numero de Exemplar maior que 0')
                return
            else:
                print('Cadastrado com Sucesso!')
            dicionario_livro= {'codigo'  : codigo,
                            'Titulo'  : titulo,
                            'Autor'   : autor,
                            'Numero de Exemplares' : numeroDeExemplares}
            lista_livro.append(dicionario_livro.copy())
        except ValueError:
            print('ATENÇÃO!!! ENTRE com valor NÚMERICO ')
        return
#------FIM DE CADASTRAR_LIVROS()------

#------INICIO DE Consultar_LIVROS()------
def consultar_livro():
    print('----Bem-vindo ao menu de Consultar livros----')
    while True:
        opcao_consultar = input('\n Escolha a opção desejada: \n'+
                            '1 - Consultar TODOS os livros \n'+
                            '2 - Consultar livro por TITULO \n'+
                            '3 - Consultar livro por AUTOR \n'+
                            '4 - Retornar \n'+
                            '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção Consultar TODOS os livros')
            for livro in lista_livro: #livro vai varrer toda lista de livros
                print(50*'-')
                for key, value in livro.items():#varrer todos os conjuntos chave e valor do dicionario livro
                    print('{}: {}'.format(key,value))
                print(50*'-')
        elif opcao_consultar=='2':
            print('Você escolheu a opção Consultar livro por TITULO')
            titulo_desejado=input('Entre com TITULO desejado \n')
            for livro in lista_livro:
                if livro['Titulo'] == titulo_desejado:#o valor de campo titulo desse dicionario é igual o titulo desejado
                    for key, value in livro.items(): #varrer todos os conjuntos chave e valor do dicionario livro
                        print('{}: {}'.format(key,value))


        elif opcao_consultar=='3':
            print('Você escolheu a opção Consultar livro por AUTOR')
            autor_desejado=input('Entre com AUTOR desejado \n')
            for livro in lista_livro:
                if livro['Autor'] == autor_desejado: #o valor de campo titulo desse dicionario é igual o titulo desejado
                    print(50*'-')
                    for key, value in livro.items():  #varrer todos os conjuntos chave e valor do dicionario livro
                        print('{}: {}'.format(key,value))
                    print(50*'-')

        elif opcao_consultar=='4':
            return #sai da função consultar e volta para o Main
        else:
            print('Opção Invalida. Tente novamente! \n')
            continue #volta para o incio do laço

#------FIM DE consultar LIVROS()------

#------INICIO DE remover_LIVROS()------
def remover_livro():
    print('----Bem-vindo ao menu de Remover livros----')
    valor_desejado=int(input('Entre com o CÓDIGO  do livro que deseja remover \n'))
    for livro in lista_livro:
        if livro['codigo'] == valor_desejado:
            lista_livro.remove(livro)
            print('\n Livro Removido.')
        else:
            print('Código não Encontrado!')

#------FIM DE remover_LIVROS()------

#------INICIO Main------

print(10*'=','Bem vindo ao Sistema de Catálogo de Livros',10*'=')

while True:
    opcao_principal = input('\n Escolha a opção desejada: \n'+
                            '1 - Cadastrar livro \n'+
                            '2 - Consultar Livros \n'+
                            '3 - Remover livro \n'+
                            '4 - Sair \n'+
                            '>>')
    if opcao_principal == '1':
        codigo_livro=codigo_livro + 1
        cadastrar_livro(codigo_livro)
    elif opcao_principal=='2':
        consultar_livro()
    elif opcao_principal=='3':
        remover_livro()
    elif opcao_principal=='4':
        print('Encerrando o programa...')
        break #encerra o laço principal e o programa acaba
    else:
        print('Opção Invalida. Tente novamente! \n')
        continue #volta para o incio do laço


#------FIM Main------