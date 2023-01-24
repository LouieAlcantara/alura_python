#função lambda
multiplicar = lambda x : x*2
print(multiplicar(9))

absoluto = lambda x , y : abs(x - y) < 3
print(absoluto(2,4))

operaçoes = lambda x , n : x*n+x/n
print(operaçoes(5,8))

#funçao map
base_numerica = [2,4,6,8,10]
aplicaveis = [1,2,3,4,5]
numeros_potenciais = list(map(pow,base_numerica,aplicaveis))
print (numeros_potenciais)

meus_numeros = [10,15,21,33,42,55]
map_numeros = list(map(lambda x : x*2 + 8,meus_numeros))
print(map_numeros)

#funçao filter
numero = [0,4,7,2,1,0,9,3,5,6,8,0,3]
numero = list(filter(lambda x : x != 0 ,numero ))
print(numero)

vogais = ['a', 'e', 'i', 'o', 'u']
vogais1 = ['w','y']
nomes = ['paula', 'tejano', 'jacinto', 'pinto', 'mario', 'Oscar']
print(list(filter(lambda x : x [0].lower() in vogais,'y')))
