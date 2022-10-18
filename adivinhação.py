print('-'*32)
print('Bem vindo ao jogo de adivinhação')
print('-'*32)

numero_secreto = 13
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas ):
    print('Tentativa {} de {} '.format (rodada ,total_de_tentativas))

    chute_str = input('Digite um número:')

    chute = int (chute_str)

    acertou = chute == numero_secreto
    maior   = chute >= numero_secreto
    menor   = chute <= numero_secreto

    print('Você digitou {}'.format(chute_str))

    if (acertou) :
            print('Você acertou xD')        
    else:

            if (menor) :
                print('Seu chute foi menor que o número secreto')

            elif (maior) :
                print('Seu chute foi maior que o número secreto')
        
    rodada = rodada + 1

print('FIM DE JOGO')