from PySimpleGUI import PySimpleGUI as sg
from lib.arquivo import *
from lib.interface import *

arq = 'cadastrosenhas.txt'
if not existeArqSenha(arq1):         #  => RETORNA True ou False
    criaArquivoSenhas(arq1)               #Não retorna NADA, APENAS ==> CRIA O ARQUIVO com a = open(arq, 'wt+')
                                        #e fecha o mesmo com a.close()
sg.theme( 'Reddit' )                    # 1. Escolha um tema para a sua janela (neste caso 'Reddit')
# Layout
layout = [
    [sg.Text( 'Usuário:' ), sg.Input( key='usuario',size=(20,1))],
    [sg.Text( 'senha:' ), sg.Input( key='senha', password_char='*',size=(20,1) )],
    [sg.Checkbox( 'Gravar a senha ?' )],
    [sg.Button( 'Confirmar' ), sg.Button('Sair')]
]
# Janela
janela = sg.Window( 'Tela de Login', layout )
# Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    if valores[0]:
        check = f'{valores["usuario"]};{valores["senha"]}\n'    # Usar \n para que o próximo registro seja gravado abaixo
        c = lerArquivoSenha(arq, check)
        if not c:
            nome = valores['usuario']
            senha = valores['senha']
            adicionarSenha( arq, nome, senha )
            sg.popup('Senha Cadastrada com sucesso !')
        else:
            sg.popup('Senha já existe')