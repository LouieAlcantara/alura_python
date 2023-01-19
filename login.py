import os
def add_arquivo (usuario):
    arquivo= open('login.txt', 'a')
    arquivo.write(usuario + '\n')
    arquivo.close()
    return None

sem_arquivo =os.path.isfile('login.txt')
if sem_arquivo != True:
    usuario = input('informe o usuario ')
    senha = input ('informe sua senha')
    add_arquivo(usuario)
else:
    arquivo = open('login.txt')
    linhas = arquivo.readlines()
    usuario = input('Informe o usuario ')
    senha = input ('informe sua senha')
    for i,linha in enumerate (linhas):
        nova_linha = linha.replace('\n', ' ').split()
        if usuario == nova_linha[0] and senha == nova_linha[1]:
            print('dados ok sistema acessado com sucesso')
            break
        elif i +1 == len(linhas) and usuario != nova_linha[0]:
            arquivo.close()
            add_arquivo(usuario,senha)
            print('novo usuario cadastrado')
            break
        else:
            acesso = 0
            if usuario == nova_linha[0]:
                acesso = 1
            if senha == nova_linha[1] :
                acesso += 1
            if acesso == 1:
                print('usuario ou senha esta incorreto')
                break
            else:
                print( 'verifique os dados ')
                break
    arquivo.close()