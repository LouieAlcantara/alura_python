class Conta :
    def __init__ (self, nome, numero):
        self.nome = nome
        self.numero = numero  
    def get_agencia (self):
        return self.__agencia
    def set_agencia (self, nova_agencia):
        if type(nova_agencia) == type(int):
            self.__agencia = nova_agencia
        else :print('O numero da agencia deve ser inteiro')
    def get_saldo (self):
        return self.__saldo
    def set_saldo
    agencia = property (get_agencia, set_agencia)
    saldo = property (get_saldo, set_saldo)