print('-'*34)
print('SEJA BEM VINDO')
print('-'*34)

palavra_secreta = 'banana'

enforcou = False
acertou = False

while(not enforcou and not acertou):
    chute = input('Diga uma letra')
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print('Encontrei a letra {} na posição {}'.format(letra, index))
    index = index + 1        
    print('jogando...')


print('FIM DE JOGO')