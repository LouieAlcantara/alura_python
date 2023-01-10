frase = input ('Digite uma frase ')
vogal ={'a','e','i','o','u','A','E','I','O','U'}
nvogais = 0

for letra in frase:
    if letra in vogal:
        nvogais += 1
print ('quantidade de vogais'{}.format(nvogais))