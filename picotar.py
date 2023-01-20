invalidos = []
numero_nao_valido = [254]
nova_lista = []
with open('ips.txt','r',encoding='utf8') as meus_ips:
    lista_ips = meus_ips.readlines()
    for linha in lista_ips:
        nova_linha = linha.replace('\n', '').split('.')
        del nova_linha[3]
        del nova_linha [2]
        del nova_linha [1]
        mudar_tipo = int(nova_linha[0])
        nova_lista.append(mudar_tipo)
        nova_lista.sort()

    print(nova_lista)

    for invalido in nova_lista:
        if invalido > 254:
            numero = invalido
            print(f'invalidos {numero}')
        else:
            numero = invalido
            print(f'esses numeros sao validos {numero}')
