from PySimpleGUI import PySimpleGUI as sg
from lib.interface import *
from lib.arquivo import *


#Programa Principal - inicio

arq = 'cadcli.txt'
arq1= 'cadastrosenhas.txt'

if not existeArq(arq):
    criaArquivo(arq)
if not existeArqSenha(arq1):
    criaArquivoSenhas(arq1)

janelamenuprincipal = None
janelaEntrarCodcli = None
janelaExibirCli = None
janelaAlteraCli = None
janelaCadastro = None
relatorioCli = None
janelaInformaCodigo = None
gravaRegAlterado = None

janelaLogin = janelaLogin()      #Início do programa - a variável janelaLogin recebe o retorno da função janelaLogin() que
while True:                      #é a própria janela de Login e Senha
    window, evento, valor = sg.read_all_windows()
    if window == janelaLogin and evento == 'Sair' or evento == sg.WIN_CLOSED:
        break
    elif window == janelaLogin and evento == 'Continuar':
        if valor['login'].strip() == '' :
            sg.popup('Por favor, digite seu Login')
            janelaLogin.un_hide()
        elif valor['senha'].strip() == '':
            sg.popup( 'Por favor, digite sua Senha' )
            janelaLogin.un_hide()
        else:
            check = f'{valor["login"]};{valor["senha"]}\n'
            c = lerArquivoSenha( arq1, check )
            if c:
                janelamenuprincipal = menuPrincipal()   # Caso o Login e Senha estejam cadastrados, é chamado o Menu Principal
                janelaLogin.hide()                      # A variável janelamenuprincipal recebe da função menuPrincipal()
            else:                                       # a própria janela Menu Principal no return da função
                sg.popup('Usuário ou Senha inválidos ! Entre em contato com o Admin')
                janelaLogin.un_hide()
    if window == janelamenuprincipal and evento == 'Sair' or evento == sg.WIN_CLOSED:
        break
    if window == janelamenuprincipal and evento == 'Confirmar':
        if valor["opcao"].strip() == "":
            sg.popup("Escolha uma opção !")
            janelamenuprincipal.un_hide()
        elif valor["opcao"] == '1':
            janelaEntrarCodcli = informaCodigo()
            janelamenuprincipal.hide()
            while True:
                window, evento, valor = sg.read_all_windows()
                check = valor["codcli"]
                check = check.strip()
                if window == janelaEntrarCodcli and evento == 'Voltar':
                    janelamenuprincipal.un_hide()
                    janelaEntrarCodcli.hide()
                    break
                elif window == janelaEntrarCodcli and evento == sg.WIN_CLOSED:
                    janelamenuprincipal.un_hide()
                    janelaEntrarCodcli.hide()
                    break
                elif window == janelaEntrarCodcli and check == '':
                    sg.popup( 'Informe o código do Cliente' )
                else:
                    janelaExibirCli = exibirCliente( arq, check )
                    janelaEntrarCodcli.hide()
                    while True:
                        window, evento, valor = sg.read_all_windows()
                        if window == janelaExibirCli and evento == 'Voltar':
                            janelaEntrarCodcli.un_hide()
                            janelaExibirCli.hide()
                            break
                        elif window == janelaExibirCli and evento == sg.WIN_CLOSED:
                            janelaEntrarCodcli.un_hide()
                            janelaExibirCli.hide()
                            break
                        elif window == janelaExibirCli :
                            sg.popup( 'Informe o código do Cliente' )
                        else:
                            janelaExibirCli
                            janelaEntrarCodcli.hide()
        elif janelamenuprincipal and valor["opcao"] == '2':
            janelaCadCliente = janelaCadCli(arq)
            janelamenuprincipal.hide()
            while True:
                window, evento, valor = sg.read_all_windows()
                if window == janelaCadCliente and evento == sg.WIN_CLOSED:
                    janelamenuprincipal.un_hide()
                    janelaCadCliente.hide()
                    break
                elif window == janelaCadCliente and evento == 'Voltar':
                    janelamenuprincipal.un_hide()
                    janelaCadCliente.hide()
                    break
                elif window == janelaCadCliente and evento == "Gravar":
                    gravaNovoCli(arq, valor)
                    janelamenuprincipal.un_hide()
                    janelaCadCliente.hide()
                    break
        elif valor["opcao"] == '3':
            janelaEntrarCodcli = informaCodigo()
            janelamenuprincipal.hide()
            while True:
                window, evento, valor = sg.read_all_windows()
                if window == janelaEntrarCodcli and evento == 'Voltar' or evento == sg.WIN_CLOSED:
                    janelamenuprincipal.un_hide()
                    janelaEntrarCodcli.hide()
                    break
                if window == janelaEntrarCodcli and evento == 'Confirmar':
                    if valor['codcli'].strip() == '':
                        sg.popup( '<<<<< Por favor, digite o código do cliente ! >>>>>' )
                        janelaEntrarCodcli.un_hide()
                    else:
                        verificação = checarCli2( arq, valor["codcli"] )
                        if verificação:
                            janelaAlteraCli = alterarArquivoCli( valor["codcli"] )
                            janelaEntrarCodcli.hide()
                            while True:
                                window, evento, valor = sg.read_all_windows()
                                if window == janelaAlteraCli and evento == 'Voltar' or evento == sg.WIN_CLOSED:
                                    janelaEntrarCodcli.un_hide()
                                    janelaAlteraCli.hide()
                                    break
                                elif window == janelaAlteraCli and evento == "Alterar":
                                    alteraLinhaCli( arq, valor )
                                    #janelamenuprincipal.un_hide()
                                    janelaEntrarCodcli.un_hide()
                                    janelaAlteraCli.hide()
                                    break
                        else:
                            sg.popup( '<<<<< Código do cliente não encontrado ! >>>>>' )
                            janelaEntrarCodcli.un_hide()

        elif valor["opcao"] == '4':
            relatorioClientes(arq)
            janelamenuprincipal.un_hide()

        elif valor["opcao"] == '5':
            break




