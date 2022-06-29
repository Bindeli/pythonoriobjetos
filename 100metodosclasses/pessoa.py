class Pessoa:
    ano_atual = 2022 # isso é um atributo de classes
    # que está acessível pela classe pessoa

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self): # para chamar esse método, eu preciso passar uma instância, que é self
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
#--------------------------------------------------------------------------------------------------------------

pessoa_1 = Pessoa('Lucas', 25)
pessoa_1.get_ano_nascimento()
print(f'Ano atual : {Pessoa.ano_atual}')
print(f'Idade de Pessoa 1 : {pessoa_1.idade}')
pessoa_1.get_ano_nascimento()

#--------------------------------------------------------------------------------------------------------------

print(f'\nAgora utilizando o método de classe:')
pessoa_2 = Pessoa.por_ano_nascimento('Joao', 1998)
print(f'Idade da Pessoa {pessoa_2.nome} : {pessoa_2.idade}')
pessoa_2.get_ano_nascimento()

#--------------------------------------------------------------------------------------------------------------

"""
Um método de classe é similar a esse atributo de classe, 'no exemplo, ano_atual'

Exemplo de uso:
Quero criar um método factory que gera outro objeto, que crie a pessoa baseado no ano de nascimento dela, e
não de idade

E para isso posso utilizar um método de classe

Vamos criar uma função dentro da classe, chamada por_ano_nascimento, e em cima dela, inserir @classmethod
e dentro do parênteses, invés de se referir a instância, iremos colocar 'cls' , se referindo à classe
pode ser qualquer nome que eu quiser, só não pode ser 'class', pois é uma palavra reservada para criar classes

Todo mundo utiliza 'cls'
"""

#--------------------------------------------------------------------------------------------------------------

"""
E Quando eu devo utilizar o método de classe e um método de instância? 

Só pensar se esse método que eu estou criando está relacionado a classe em geral ou molde em geral, 
ou à instância, ele é específico de cada objeto, que cada objeto terá um valor diferente para esse método
que eu estou gerando e é aqui que eu decido qual eu irei utilizar.
"""
#--------------------------------------------------------------------------------------------------------------



