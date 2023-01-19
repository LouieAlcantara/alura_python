try:
    print(2+ 'casa')
except:
    print('ops deu erro')

try:
    print(2+2)
except:
    print('ops deu erro')

try:
    print(x)
except:
    print('Variavel nao foi definida')
finally:
    print('try foi concluido')

try:
    print('Hello')
except:
    print('Deu algo errado')
else:
    print('nada deu errado')

