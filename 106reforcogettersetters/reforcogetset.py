"""
SETTER = Set , configurando um valor (=)
Quando você fala que seu atributo é igual a alguma coisa, você está passando pelo setter

GETTER = Get, obter um valor
GETTER = Sua função é retornar o valor daquela coisa que configuramos no setter

GETTER = Lê
SETTER = Configura

Podemos criar o getter sozinho sem o setter, porém não podemos criar um Setter sozinho

Quando falamos de getter e setter, estamos falando de funções.

"""

class Pessoa:

    def __init__(self):
        self.atributo = 'inicio'
    # método é uma função que está dentro da classe
    # def nome(self):
    #     return 'Lucas'
    # para transformar isso em um getter, eu crio um decorador em cima como @property
    @property
    def nome(self):
        return 'Lucas Bindeli'

    #O setter configura o valor
    # para criar um setter em python, eu tenho que pegar o nome de algum método que eu utilize como property
    # e colocar .setter
    # a função do setter geralmente vai receber um valor para você configurar
    @nome.setter
    def nome(self, nome):
        self.atributo = nome

pessoa_1 = Pessoa()
print(pessoa_1.atributo)
print(pessoa_1.nome)

# Você está indicando para o Python, que você quer que aquela função se comporte como um atributo















