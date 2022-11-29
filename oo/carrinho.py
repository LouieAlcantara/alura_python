class Carro ():
    def __init__(self, modelo, cor, consumo):
        self.modelo = modelo
        self.cor = cor
        self.consumo = consumo 
        self.tanque_litros = 0
    def pintar (self):
        sua_cor = int(input('escolhar: [1]prata, [2] preto, [3]branco'))
        if sua_cor != 1 and sua_cor != 2 and sua_cor != 3 :
            print ('invalido')
        else:
            lista_de_cores = [0, 'prata', 'preto', 'branco']
            self.cor = lista_de_cores[sua_cor]

    def pintado (self):
        return (f'a cor do seu carro é{self.cor}')

    def verificar_tanque(self,litros):
        capacidade_tanque = 40
        if ((self.tanque_litros + litros)<= capacidade_tanque) :
            return litros
        else:
            return(capacidade_tanque - self.tanque_litros)

    def abastecer (self, litros):
        abastecer = self.verificar_tanque(litros)
        self.tanque_litros += abastecer
        print(f'seu tanque foi abastecido com {litros} litros de combustivel e tem {self.tanque_litros} litros')
        if abastecer <= self.tanque_litros :
            print('Só é possivel encher até que 40 litros')
        else:
            return abastecer
    
    def pode_andar (self, distancia):
      consumo = (distancia/self.consumo)
      return (self.tanque_litros>= consumo) 

    def andar (self, distancia):
        if(self.pode_andar(distancia)):
            self.tanque_litros -= (distancia/self.consumo)
        else:
            print(f'combustivel insuficiente para andar {distancia}km')

    def mostrar_tanque (self):
        print(f'restam {self.tanque_litros:.2f} litros no combustivel no tanque')


palio = Carro('esx','branco',12)
palio.pintar()
print(palio.pintado())
palio.abastecer(8)
palio.andar(124)
palio.mostrar_tanque()
palio.abastecer(25)
palio.andar(150)
palio.mostrar_tanque()