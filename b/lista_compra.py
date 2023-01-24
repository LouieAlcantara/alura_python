with open('lista_compras.txt','r',encoding= 'utf-8') as lista_compras:
    for linhas in lista_compras:
        aumento =[{map(lambda x : x + 10/100,lista_compras)}]
        print(aumento)