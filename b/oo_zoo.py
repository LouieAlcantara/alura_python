#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# que demonstre um jardim zoológico. Nele foi definido a seguinte herança Animal(super) AnimalOrcamento(sub) ListaOrçamentaria(independente)
# na super monte um animal com seus atributos necessários e as necessidades para que o mesmo seja cuidado.
# Você deve implementar um método que mostre quais animais têm a “vacina XYZ” para tomar e seus valores.
# na sub você deve implementar um método OrcamentoGastosAnimal que retorna o orçamento previsto para gastos de um animal no zoológico.
# na lista faça um método que receba como parâmetro uma lista e que implementa o animal, o orçamento e seus gastos
# OBS: Implemente outros atributos e métodos para deixar a estrutura valida
# OBS: Veja a possibilidade de utilizar os métodos mágicos
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça as impressões necessárias


class Animal():
    def __init__ (self, especie, altura, peso):
        self.especie = especie
        self.altura = altura
        if type(peso) == type(float()) :
            self.__peso = peso
        else:
            raise ValueError ('permitido apenas float')  
        self.alimento = 0
        self.banho = 0

        
    def get_peso (self):
        return self.__peso
    
    def set_peso (self, novo_peso):
        if type(novo_peso) == type(float()):
            self.__peso == novo_peso
        else:
            raise ValueError('permitido apenas float')

    def verificacao_peso (self):
        if self.__peso < 0.150 :
            raise ValueError('nao é possivel ter um animal nesse peso')
        else :
            return ('peso esta estavel')
    
    def vacinas_dispinveis (self):
        vacinas = ['raiva', 'carrapato', 'gripe']
    
    def vacinacao (self, idade, sexo, vacina):
        self.idade = idade
        self.sexo = sexo 
        self.vacina = vacina

    def verificacao_vacina(self):
        if self.vacina<=2:
            return ('liberado tomar vacina')
        else:
            raise ValueError('vacina nao disponivel')
    def alimentar (self):
        self.alimento + 40
    
    def cheio (self):
        if self.alimento>= 100:
            print ('estou cheio')
        else:
            print ('estou com fome')
    def limpar(self):
        self.banho + 60 
    
    def verificacao_de_banho (self):
        if self.banho >= 120:
            print ('estou limpo')
        else:
            print (' nao estou limpo')

    def __str__ (self):
        return (f'O(a) {self.especie} tem altura {self.altura}, esta com alimentado {self.alimento} e esta com {self.banho}')
    peso = property(get_peso, set_peso)

class AnimalOrcamento(Animal):
    def orcamento (self):
        (self.__peso / self.altura) *100
    
    def gastos_reais ():
        pass




macaco = Animal('macaco', 0.60, 0.100 )
macaco.vacinacao(18,'femea', 2)
macaco.limpar()
macaco.alimentar()


