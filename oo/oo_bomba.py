#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe BombaCombustivel abaixo sabemos que é uma bomba de gasolina e:
# atributos: valor_do_litro e quantidade_de_combustivel
# todos atributos encapsulados fortemente
# métodos abaixo:
# abastecer_a_bomba - esse método abastece a bomba para iniciar a venda
# abastecer_veiculo_valor – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_veiculo_litro – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente
# alterar_valor – altera o valor do litro do combustível
# alterar_quantidade_combustivel – altera a quantidade combustível restante na bomba
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
# OBS: Faça a impressão dos elementos

class BombaCombustivel :
    def __init__ (self,):
        self.__valor_do_litro = 3.0
        self.__quantidade_de_combustivel = 0
        self.quantidade_litro = 0

    def get_valor_do_litro (self):
        return self.__valor_do_litro 
    def set_valor_do_litro (self, novo_valor):
            if type(self.__valor_do_litro) == type(float()):
                self.__valor_do_litro = novo_valor
            else:print('o valor deve ser em float')

    def get_quantidade_de_combustivel (self):
        return self.__quantidade_de_combustivel
    def set_quantidade_de_combustivel (self, nova_quantidade):
        if type(self.__quantidade_de_combustivel) == type(float()):
                self.__quantidade_de_combustivel = nova_quantidade
        else:print('o valor deve ser em float ')
 
    def limite_bomba (self, litros):
        limite_bomba = 150
        if self.quantidade_litro + litros <= limite_bomba:
            return litros
        else: return self.quantidade_litro - limite_bomba

    def abastecer_bomba (self, litros):
        self.abastecer = self.limite_bomba
        valor =self.quantidade_litro + litros
        if type(valor) == type(float):
            print(f'Bomba foi abastecida com {litros} litros')
        else: print('So é possivel abastecer com numeros float')

    def abastecer_veiculo_valor (self, dinheiro):
        abastecer_veiculo = dinheiro * self.__valor_do_litro
        if abastecer_veiculo > 150:
            print(f'Não é possivel abastecer {abastecer_veiculo} litros pois não tem disponivel na bomba')
        else: print (f'O veiculo foi abastecido com {abastecer_veiculo} litros')
    
    def abastecer_veiculo_litro (self, litro):
        self.abastecer_veiculo = litro * self.valor_do_litro
        if litro > 150:
            print(f'Não é possivel abastecer {litro} litros pois não tem disponivel na bomba')
        else: print (f'é necessario pagar {self.abastecer_veiculo} reais')
    
    def altera_valor (self, novo_valor):
        if type(novo_valor) == type (float()):
            print(f'voce modificou o valor para {novo_valor}')
        else : 
            print ('não é possivel modificar')
        
    def altera_combustivel (self):
        pass
    
    valor_do_litro = property (get_valor_do_litro, set_valor_do_litro)
    quantidade_de_combustivel = property (get_quantidade_de_combustivel, set_quantidade_de_combustivel)

gasolina = BombaCombustivel()
gasolina.set_valor_do_litro(3.0)
print(gasolina.get_valor_do_litro())
gasolina.abastecer_bomba(0.9)
gasolina.abastecer_veiculo_valor(678)
gasolina.abastecer_veiculo_litro (9)
gasolina.altera_valor (9.0)
gasolina.altera_combustivel()