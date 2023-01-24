alfabeto = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
vogais =['a','e','i','o','u']
nomes = open('lista_nomes.txt','r',encoding='utf-8')
lista_nomes = nomes.readlines()
for letras in lista_nomes:
    