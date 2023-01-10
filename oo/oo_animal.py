#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na Super classe Animal com os atributos: nome, peso, energia:
# implemente os métodos abaixo:
# correr - esse método diminui 100g do peso e 10 pontos de energia a cada 1000m
# dormir - esse método engorda o animal 150g e aumenta 15 pontos de energia a cada 5 horas dormidas
# você deve criar duas subclasses a sua escolha 
# OBS: Deve ser criado o POLIMORFISMO do ambiente
# OBS: Deve ser feito os GETs e SETs
# OBS: Não esqueça das validações dos métodos
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos


class Animal():
    def __init__ (self,nome, peso):
        self.__nome = nome
        self.__peso = peso
        self.energia = 100 
    def __str__ (self):   
        return (f'Meu nome é {self.__nome}, peso {self.__peso} e o total de energia é {self.energia}')
    def get_nome (self):
        return self.__nome 
    
    def set_nome (self, novo_nome):
        if type(novo_nome) == type(float):
            self.__nome = novo_nome
            print(f'Meu novo nome é {novo_nome}')
        else:
            raise ValueError('Nao é possivel escrever o nome')
    
    def get_peso(self):
        return self.__peso

    def set_peso (self, novo_peso):
        if type(novo_peso) == type(float):
            self.peso = novo_peso
        else:
            raise ValueError('so é possivel em float')

    def converter_gramas (self,):
        self.__peso = self.__peso * 1000
        return self.__peso

    def converter_distancia(self, km):
        self.distancia_metros = km * 1000
    def correr (self):
        if self.distancia_metros > 10000:
            raise ValueError ('nao é possivel andar essa distancia')
        else:
            self.km = self.distancia_metros / 1000
            self.__peso = (self.__peso - (100 * self.distancia_metros) / 1000 ) /1000
            self.energia = (self.energia - (10 * self.distancia_metros) / 1000) 
            print(f'voce correu {self.km} km, e sua energia é {self.energia} e seu peso é {self.__peso}kg')
    
    def converter_hora (self,hora):
        self.hora = hora
        self.minuto = hora * 60

    def dormir (self):
        if self.minuto > 840 :
            raise ValueError ('voce quer dormir alem da conta')
        else:
             self.__peso = (self.__peso + (0.150 * self.distancia_metros) / 1000) 
             self.energia = (self.energia + (15 * self.distancia_metros) / 1000) 
        if self.energia <=100:
             print(f'voce dormiu {self.hora} horas e seu peso esta {self.__peso} kg e sua energia esta {self.energia}')
        else:
            print(f'voce dormiu {self.hora} horas e seu peso esta {self.__peso}kg e sua energia esta 100 ')
    nome = property(get_nome, set_nome)
    peso = property (get_peso, set_peso)


class Pato (Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)
    
    def __str__(self):
        return f'Seu pato se chama {self.nome}, pesa {self.peso}kg e energia {self.energia}'

class Cachorro (Animal):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def __str__(self):
        return f'Seu cao se chama {self.nome}, pesa {self.peso}kg e energia {self.energia}' 



gato = Animal('leo',5)
gato.converter_distancia(2)
gato.converter_gramas()
gato.correr()
gato.converter_hora(7)
gato.dormir()
carlos = Pato('carlos',9)
print(carlos)
carlos.converter_distancia(1)
carlos.converter_gramas()
carlos.correr()
