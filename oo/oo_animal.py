#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na Super classe Animal abaixo sabemos que ela tem:
# duas subclasses: Pessoa e Cao
# você deve definir onde e como serão criados os atributos e os métodos dessas SUPER e SUBs
# atributos: nome, idade, peso e altura
# métodos abaixo:
# envelhecer - esse método aumenta a idade de "Pessoa" em 1 ano e de "Cao" em 7 anos
# engordar - amenta o peso de "Pessoa" em 300g por 1 kilo e "Cao" 150g por 1Kg comido 
# correr – marque com tempo
# emagrecer – diminui o peso de "Pessoa" em 400g a cada 1h corrida e "Cao" 500g a cada 1h corrida
# crescer – cada ano que passar "Pessoa" cresce 0,5cm e "Cao" cresce 3,5cm
# OBS: Deve ser criado o POLIMORFISMO do ambiente
# OBS: Pessoa só cresce até 21 anos e Cao até 14 anos
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos

class Animal:
    pass

class Pessoa(Animal):
    pass

class Cao(Animal):
    pass