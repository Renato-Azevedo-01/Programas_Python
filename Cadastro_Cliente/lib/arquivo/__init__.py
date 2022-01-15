from lib.interface import *
from PySimpleGUI import popup
import shutil
import tempfile

arq1 = 'cadastrosenhas.txt'

def existeArq(arq):
    try:
        a = open(arq,'rt')
        a.close()
    except FileNotFoundError:
        print('ERRO ! Arquivo não encontrado')
        return False
    else:
        return True


def criaArquivo(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print(f'ERRO ao criar o arquivo {arq} ')
    else:
        print(f'Arquivo {arq} criado com sucesso !')


def existeArqSenha(arq1):
    try:
        a = open( arq1, 'rt' )
        a.close()
    except FileNotFoundError:
        print( 'ERRO ! Arquivo de senhas não encontrado' )
        return False
    else:
        return True


def criaArquivoSenhas(arq1):
    try:
        a = open( arq1, 'wt+' )
        a.close()
    except:
        print( f'ERRO ao criar o arquivo {arq1} ' )
    else:
        print( f'Arquivo {arq1} criado com sucesso !' )


def lerArquivoSenha(arq1, check):                       #primeiro acesso ao arquivo de Login e Senhas cadastradas
    ok = False                                          #recebe como parâmetros o arquivo cadastrosenhas.txt e
    try:                                                #a junção do Login;Senha digitados na interface janelaLogin()
        a = open(arq1, 'rt')
        a.close()
    except:
        print('ERRO ao ler arquivo de senhas')
    else:                                                   #retorna True se o parâmetro check(login;Senha) for
        if check in a:                                      #encontrado em uma das linhas do arquivo cadastrosenhas.txt
            ok = True                                       #caso contrário, retornará False.
    return ok                                               # => Neste caso, a chamada desta janela DEVE ser feita por
                                                            # uma variável. Ex: c = lerArquivoSenha(arq1, check) pois
                                                            #ela receberá True ou False lá no programa principal.
def adicionarSenha(arq1, login='desconhecido', senha='0'):
    try:
        a = open(arq1, 'at')
    except:
        print('ERRO ao inserir dados no arquivo')
    else:
        try:
            a.write(f'{login};{senha}\n')
        except:
            print( 'Houve1 erro na hora de escrever os dados' )
        else:
            print(f'Cadastro1 de {login} realizado com sucesso!')
            a.close()


def lerArquivoCli(arq,cod):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO ao ler dados no arquivo')
    else:
        try:
            a.read(arq)
        except:
            print( 'Houve erro na hora de ler os dados' )
            return False
        else:
            if cod in arq:
                return True
                a.close()


def gravaRegAlterado(arq, cad ):                # Este !!!
    try:
        a = open( arq, 'rt' )
    except:
        print( 'ERRO ao inserir dados no arquivo' )
    else:
        while True:
            ok = False
            for lin in a:
                reg = lin.split( ';' )
                if cad["codcli"].strip() == reg[0]:
                    ok = True
                    break
            break
        if ok == False:
            a = open( arq, 'at' )
            reg = f'{cad["codcli"]};{cad["nomecli"]};{cad["dtnasc"]};{cad["cpf"]};{cad["identidade"]};{cad["endereco"]};{cad["numero"]};{cad["complemento"]};{cad["bairro"]};{cad["uf"]};{cad["cep"]};{cad["cel"]};{cad["tel"]};{cad["estcivil"]};{cad["situacao"]}'
            a.write(f'{reg}\n')
            popup( '<<<<<<< Cadastro realizado com sucesso! >>>>>>>' )
        else:
            popup( '<<<<<<< Código já cadastrado! >>>>>>>' )
        a.close()


def lerArquivoSenha(arq1,check):
    ok = False
    try:
        a = open( arq1, 'rt' )
    except:
        print( 'ERRO ao ler arquivo' )
    else:
        if check in a:
            ok = True
    return ok

def gravaNovoCli(arq, cad ):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO ao inserir dados no arquivo')
    else:
        while True:
            ok = False
            for lin in a:
                reg = lin.split(';')
                if cad["codcli"].strip() == reg[0]:
                    ok = True
                    a.close()
                    break
            break
        if ok == False:
            a = open(arq, 'at')
            reg = f'{cad["codcli"]};{cad["nomecli"]};{cad["dtnasc"]};{cad["cpf"]};{cad["identidade"]};{cad["endereco"]};' \
                  f'{cad["numero"]};{cad["complemento"]};{cad["bairro"]};{cad["uf"]};{cad["cep"]};{cad["cel"]};{cad["tel"]};' \
                  f'{cad["estcivil"]};{cad["situacao"]}'
            a.write(f'{reg}\n')
            popup('<<<<<<< Cadastro realizado com sucesso! >>>>>>>')
        else:
            popup( '<<<<<<< Código já cadastrado! >>>>>>>' )
        a.close()
    with open( arq, "rt" ) as a, tempfile.NamedTemporaryFile( "wt", delete=False ) as cadtemp:
        for lin in a:
            cad = lin.split( ';' )
            if cad[0].strip() != '':
                cadtemp.write( lin )

        # move o arquivo temporário para o original
    shutil.move( cadtemp.name, arq )




