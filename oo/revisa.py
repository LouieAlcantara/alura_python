class Livro :
    def __init__ (self, nome, qtdpaginas, autor):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
    
    def get_preco (self):
        return self.__preco
    
    def set_preco (self, novo_preco):
        if type(novo_preco) == type (float()):
            self.__preco = novo_preco
        else :
            print('O preço deve ser em float')
    def __str__ (self):
        return (f'O {self.__class__.__name__} {gibi.nome} do autor {gibi.autor} tem {gibi.qtdpaginas} paginas e custa RS {gibi.preco} ')
    preco = property(get_preco, set_preco)

gibi = Livro('Turma da monica', 22, 'Mauricio de Sousa')
print('='*20)
gibi.set_preco (7.5)
print(gibi.get_preco())
print('='*20)
print('='*20)
print(gibi)
print('='*20)