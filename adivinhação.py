print('-'*30)
print('Bem vindo ao jogo de adivinhação')
print('-'*30)

numero_secreto = 13

chute_str = input('Digite um número:')

chute = int (chute_str)

print('Você digitou {}'.format(chute_str))

if numero_secreto == chute :
    print('Você acertou xD')
elif chute <= numero_secreto :
    print('Seu chute foi menor que o número secreto')
else :
    print('Seu chute foi maior que o número secreto')

print('FIM DE JOGO')