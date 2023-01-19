
valores = open('valores.txt', 'r')
pagamento = open('pagamentos.txt', 'w') 

for  linha in  valores :
    nomes = input('Digite o nome do funcionario:')
    pagamento.write (nomes + ':' + linha + '\n')

valores.close()
pagamento.close()
        
pagamento = open('pagamentos.txt', 'r')

for linha in pagamento:
    print(linha)

pagamento.close()