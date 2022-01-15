from PySimpleGUI import PySimpleGUI as sg
from lib.arquivo import *
#from Ex136_Cadastro_Cliente import *
from lib.interface import *
import shutil
import tempfile


#arq1 = 'cadastrosenhas.txt'

def janelaLogin():                                                          #primeira janela a ser chamada (Não recebe parâmetros)
    sg.theme( 'Reddit' )

    layout1 = [
        [sg.Text(text='Usuário')],
        [sg.Text(text='Login'),sg.Input(key='login',size = (30,1))],
        [sg.Text(text='Senha'), sg.Input(key='senha',password_char='*',size = (29,1))],

        [sg.Button('Continuar'),sg.Button('Sair')]
               ]
    return sg.Window('Cadastro de Clientes',layout=layout1, finalize=True)  #retorna a janela de Login

def janelaLoginAdm():                             #Somente para cadastar senha (Grava_Senhas.py) pelo Administrador
    sg.theme( 'Reddit' )
    layout1 = [
        [sg.Text(text='Login Administrador')],
        [sg.Text(text='Administrador'),sg.Input(key='loginadm',size = (20,1))],
        [sg.Text(text="Senha Adm"), sg.Input(key='senhaadm',size = (10,1))],

        [sg.Button('Continuar'),sg.Button('Sair')]
               ]
    return sg.Window('Cadcli - LoginAdm',layout=layout1, finalize=True)

def verificaSenha(valores):
    print(valores)
    check = f'{valores["login"]};{valores["senha"]}\n'


def menuPrincipal():                                                    #Segunda janela a ser chamada (Não recebe parâmetros)
    sg.theme('Reddit')

    layout1 = [
        [sg.Text( 'MENU PRINCIPAL' )],

        [sg.Text( "1. Ler Cliente" )],
        [sg.Text( "2. Inserir Cliente" )],
        [sg.Text( "3. Alterar Dados do Cliente" )],
        [sg.Text( "4. Gerar Relatório de Clientes" )],
        [sg.Text( "5. Sair" )],

        [sg.Text( 'Opção => ' ), sg.Input( key="opcao",size=(2,1) )],
        [sg.Button( 'Confirmar' ), sg.Button( 'Sair' )]
            ]
    return sg.Window('Cadcli - Menu Principal', layout=layout1, finalize=True )  # retorna a uma variável a propria tela


def informaCodigo():                # É chamada quando a opção 1 do Menu Principal é confirmada
    sg.theme('Reddit')

    layout1 = [
        [sg.Text( text='Código' ), sg.Input( key='codcli', size=(5, 1))],
        [sg.Button( 'Confirmar' ), sg.Button( 'Voltar' )]
            ]
    return sg.Window( 'Cadcli - Informar Código', layout=layout1, finalize=True )


def checarCli(arq, check):
    try:
        a = open( arq, 'rt' )
    except:
        print( 'ERRO ao ler arquivo' )
    else:
        ok = False
        for lin in a:
            lista = lin.split(';')
            lista[14] = lista[14].replace('\n','')
            if check == lista[0]:
                ok = True
        return ok

def checarCli2(arq, check):
    try:
        a = open( arq, 'rt' )
    except:
        print( 'ERRO ao ler arquivo' )
    else:
        ok = False
        for lin in a:
            lista = lin.split(';')
            if check == lista[0]:
                ok = True
        return ok


def janelaCadCli(arq):
    sg.theme( 'Reddit')
    a = open( arq, 'rt' )

    layout1 = [
        [sg.Text('Código'), sg.Input(key='codcli',size=(5,1))],
        [sg.Text( 'Nome' ), sg.Input( key='nomecli', size=(50, 1) )],
        [sg.Text( 'Data de Nascimento' ), sg.Input( key='dtnasc', size=(10, 1) )],
        [sg.Text( 'CPF' ), sg.Input( key='cpf', size=(11, 1) )],
        [sg.Text( 'Identidade' ), sg.Input( key='identidade', size=(9, 1) )],
        [sg.Text( 'Endereço' ), sg.Input( key='endereco', size=(30, 1) )],
        [sg.Text( 'Número' ), sg.Input( key='numero', size=(5, 1) )],
        [sg.Text( 'Complemento' ), sg.Input( key='complemento', size=(15, 1) )],
        [sg.Text( 'Bairro' ), sg.Input( key='bairro', size=(15, 1) )],
        [sg.Text( 'UF' ), sg.Input( key='uf', size=(2, 1) )],
        [sg.Text( 'CEP' ), sg.Input( key='cep', size=(8, 1) )],
        [sg.Text( 'Celular' ), sg.Input( key='cel', size=(15, 1) )],
        [sg.Text( 'Telefone' ), sg.Input( key='tel', size=(15, 1) )],
        [sg.Text( 'Estado Civil' ), sg.Input( key='estcivil', size=(15, 1) )],
        [sg.Text( 'Situação' ), sg.Input( key='situacao', size=(15, 1) )],

        [sg.Button('Gravar'), sg.Button('Voltar')]
            ]
    return sg.Window( 'Cadcli - Cadastro de Clientes', layout=layout1, finalize=True )


def alteraCli(codcli):
    a = open('cadcli.txt', 'rt')

    for lin in a:
        if codcli in lin:
            cad = lin.split(';')
            layout1 = [
                [sg.Text( 'Código' ), sg.Input(cad[0],key = 'codcli', size = (5, 1) )],
                [sg.Text( 'Nome  ' ), sg.Input(cad[1], key='nomecli', size=(50, 1) )],
                [sg.Text( 'Data de Nascimento' ), sg.Input(cad[2], key='dtnasc', size=(10, 1) )],
                [sg.Text( 'CPF   ' ), sg.Input( cad[3],key='cpf', size=(11, 1) )],
                [sg.Text( 'Identidade' ), sg.Input(cad[4], key='identidade', size=(9, 1) )],
                [sg.Text( 'Endereço' ), sg.Input( cad[5],key='endereco', size=(30, 1) )],
                [sg.Text( 'Número' ), sg.Input( cad[6],key='numero', size=(5, 1) )],
                [sg.Text( 'Complemento' ), sg.Input( cad[7],key='complemento', size=(15, 1) )],
                [sg.Text( 'Bairro' ), sg.Input( cad[8],key='bairro', size=(15, 1) )],
                [sg.Text( 'UF    ' ), sg.Input( cad[9],key='uf', size=(2, 1) )],
                [sg.Text( 'CEP   ' ), sg.Input( cad[10],key='cep', size=(8, 1) )],
                [sg.Text( 'Celular' ), sg.Input( cad[11],key='cel', size=(15, 1) )],
                [sg.Text( 'Telefone' ), sg.Input( cad[12],key='tel', size=(15, 1) )],
                [sg.Text( 'Estado Civil' ), sg.Input( cad[13],key='estcivil', size=(15, 1) )],
                [sg.Text( 'Situação' ), sg.Input( cad[14],key='situacao', size=(15, 1) )],

                [sg.Button( 'Gravar' ), sg.Button( 'Voltar' )]
            ]
            return sg.Window( 'Cadcli - Cadastro de Clientes', layout=layout1, finalize=True )



def alterarArquivoCli(codcli):                # Este !!!
    a = open( 'cadcli.txt', 'rt' )
    for lin in a:
        if codcli in lin:
            cad = lin.split( ';' )
            layout1 = [
                [sg.Text( 'Código' ), sg.Input( cad[0], key='codcli', size=(5, 1) )],
                [sg.Text( 'Nome  ' ), sg.Input( cad[1], key='nomecli', size=(50, 1) )],
                [sg.Text( 'Data de Nascimento' ), sg.Input( cad[2], key='dtnasc', size=(10, 1) )],
                [sg.Text( 'CPF   ' ), sg.Input( cad[3], key='cpf', size=(11, 1) )],
                [sg.Text( 'Identidade' ), sg.Input( cad[4], key='identidade', size=(9, 1) )],
                [sg.Text( 'Endereço' ), sg.Input( cad[5], key='endereco', size=(30, 1) )],
                [sg.Text( 'Número' ), sg.Input( cad[6], key='numero', size=(5, 1) )],
                [sg.Text( 'Complemento' ), sg.Input( cad[7], key='complemento', size=(15, 1) )],
                [sg.Text( 'Bairro' ), sg.Input( cad[8], key='bairro', size=(15, 1) )],
                [sg.Text( 'UF    ' ), sg.Input( cad[9], key='uf', size=(2, 1) )],
                [sg.Text( 'CEP   ' ), sg.Input( cad[10], key='cep', size=(8, 1) )],
                [sg.Text( 'Celular' ), sg.Input( cad[11], key='cel', size=(15, 1) )],
                [sg.Text( 'Telefone' ), sg.Input( cad[12], key='tel', size=(15, 1) )],
                [sg.Text( 'Estado Civil' ), sg.Input( cad[13], key='estcivil', size=(15, 1) )],
                [sg.Text( 'Situação' ), sg.Input( cad[14], key='situacao', size=(15, 1) )],

                [sg.Button( 'Alterar' ), sg.Button( 'Voltar' )]
            ]
            a.close()
            return sg.Window( 'Cadcli - Alteração de Clientes', layout=layout1, finalize=True )


def linha(tam=42):
    return '-'*tam


def cabeçalho(msg):
    print(linha())
    print(f'{msg}'.center(42))
    print(linha())


def exibirCliente(arq,codcli):
    ok = False
    a = open(arq, 'rt')
    for lin in a:
        cad = lin.split(';')
        if codcli == cad[0]:
            ok = True
            layout1 = [
                [sg.Text( 'Código:       ' ), sg.Text(cad[0], size = (5, 1) )],
                [sg.Text( 'Nome:         ' ), sg.Text(cad[1], key='nomecli', size=(50, 1) )],
                [sg.Text( 'Data de Nascimento:' ), sg.Text(cad[2], key='dtnasc', size=(10, 1) )],
                [sg.Text( 'CPF:          ' ), sg.Text( cad[3],key='cpf', size=(11, 1) )],
                [sg.Text( 'Identidade:   ' ), sg.Text(cad[4], key='identidade', size=(9, 1) )],
                [sg.Text( 'Endereço:     ' ), sg.Text( cad[5],key='endereco', size=(30, 1) )],
                [sg.Text( 'Número:       ' ), sg.Text( cad[6],key='numero', size=(5, 1) )],
                [sg.Text( 'Complemento:  ' ), sg.Text( cad[7],key='complemento', size=(15, 1) )],
                [sg.Text( 'Bairro:       ' ), sg.Text( cad[8],key='bairro', size=(15, 1) )],
                [sg.Text( 'UF:           ' ), sg.Text( cad[9],key='uf', size=(2, 1) )],
                [sg.Text( 'CEP:          ' ), sg.Text( cad[10],key='cep', size=(8, 1) )],
                [sg.Text( 'Celular:      ' ), sg.Text( cad[11],key='cel', size=(15, 1) )],
                [sg.Text( 'Telefone:     ' ), sg.Text( cad[12],key='tel', size=(15, 1) )],
                [sg.Text( 'Estado Civil: ' ), sg.Text( cad[13],key='estcivil', size=(15, 1) )],
                [sg.Text( 'Situação:     ' ), sg.Text( cad[14],key='situacao', size=(15, 1) )],

                [sg.Button( 'Voltar' )]
                ]

    if ok == True:
        return sg.Window( 'Cadcli - Consulta Clientes', layout=layout1, finalize=True )
    else:
        layout2 = [
            [sg.Text('<<<<<<<Cliente não encontrado>>>>>>>')],
            [sg.Button( 'Voltar' )]
        ]

        return sg.Window( 'Cadcli - Consulta Clientes', layout=layout2, finalize=True )



def relatorioClientes(arq):
    try:
        a = open( arq, 'rt' )
    except:
        print( 'ERRO ao ler arquivo' )
    else:
        n = 1
        print('-' * 50)
        print('{: ^50}' .format("\033[1;31mCadastro de Clientes\033[m"))
        print('-' *50)
        for lin in a:
            cad = lin.replace("/n","")
            cad = lin.split( ';' )
            #cad[14] = cad[14].replace( "\n", "" )
            print(f'{n}º Registro => {cad[1]}')
            print('-' * 50)
            print( f'Código:        {cad[0]}')
            #print( f'Nome:          {cad[1]}')
            print( f'Data de Nasc:  {cad[2]}')
            print( f'CPF:           {cad[3]}')
            print( f'Identidade:    {cad[4]}')
            print( f'Endereço:      {cad[5]}')
            print( f'Número:        {cad[6]}')
            print( f'Complemento:   {cad[7]}')
            print( f'Bairro:        {cad[8]}')
            print( f'UF:            {cad[9]}')
            print( f'CEP:           {cad[10]}')
            print( f'Celular:       {cad[11]}')
            print( f'Telefone:      {cad[12]}')
            print( f'Estado Civil:  {cad[13]}')
            print( f'Situação:      {cad[14]}')
            print('-' * 50)
            n += 1
        sg.popup('<<<<< Relatório gerado com sucesso ! >>>>>')


def alteraLinhaCli(arq, valor):
    msg = ''
    indice = 0
    indicefinal = 0
    ok = False
    a = open(arq, 'rt')
    for lin in a:
        cad = lin.split( ';' )
        if valor["codcli"] == cad[0]:
            ind = indice
        indice += 1
        indicefinal += 1
    a.close()                                                      #coloquei depois
    with open(arq, "rt") as a, tempfile.NamedTemporaryFile("wt", delete=False) as cadtemp:
        for lin in a:
            cad = lin.split(';')
            if valor["codcli"] == cad[0]:
                ok = True

                msg = f'{valor["codcli"]};{valor["nomecli"]};{valor["dtnasc"]};{valor["cpf"]};{valor["identidade"]};' \
                      f'{valor["endereco"]};{valor["numero"]};{valor["complemento"]};{valor["bairro"]};{valor["uf"]};' \
                      f'{valor["cep"]};{valor["cel"]};{valor["tel"]};{valor["estcivil"]};{valor["situacao"]}'
                if ind < indicefinal:
                    cadtemp.write(f'{msg}')
                else:
                    cadtemp.write( f'{msg}\n' )
            else:
                cadtemp.write(lin)

# move o arquivo temporário para o original
    shutil.move(cadtemp.name, arq)
    if ok == True:
        sg.popup( '<<<<<<< Alteração do cliente realizada com sucesso ! >>>>>>>' )
    else:
        sg.popup( '<<<<<<< Cliente não encontrado ! >>>>>>>' )

