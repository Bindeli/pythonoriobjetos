"""
Aula 98 - Classes - Python Orientada a Objetos


"""

from pessoas import Pessoa

pessoa_1 = Pessoa('Lucas',25)
# seria a mesma coisa se eu colocasse pessoa_1.nome = 'Lucas'
pessoa_2 = Pessoa('João', 37)

# print(pessoa_1) # pessoa 1
# print(pessoa_2) # pessoa 1

# podem parecer iguais, mas estão em locais diferentes da memória

# Aqui estamos utilizando um molde para criar uma pessoa

#------------------------------------------------------------------------------------------------------------------
"""
Sabendo disso, eu posso criar uma variável que pertence somente a pessoa 1
"""

# pessoa_1.nome = 'Lucas'

"""
Não estará presente em um print solo ou em pessoa_2
Quando rode, algo como pessoa_2.nome, terá um erro de atributo, "Pessoa object has no attribute 'nome'


Variaveis de instância ou variáveis de classes, são chamados de atributo da classe

para que a pessoa 2 tenha a variável, eu posso adicionar também
"""
# pessoa_2.nome = 'João'

"""
Porém não utilizemos desta maneira, como a classe Pessoa é um molde, eu quero que cada pessoa tenha esse atributo
Além de outros atributos

Então vamos pro arquivo pessoas.py para adicionar os atributos

"""

#------------------------------------------------------------------------------------------------------------------
"""
Em pessoas criamos um método, 'falar', que irá aparecer quando chamarmos ela
Eu chamo o objeto que eu quero e o método que desejo utilizar
"""
#pessoa_1.falar()

#------------------------------------------------------------------------------------------------------------------
# Chamando a variavel com o método

# pessoa_1.__init__('Lucas', 35)

# utilizando o comendo

pessoa_1.comer('carne')
"""
Eu não quero permitir que tal pessoa coma algo duas vezes, como se tivesse comendo isso 2x ao mesmo tempo.

pessoa_1.comer('carne')
pessoa_1.comer('carne')

Então coloquei um if para aparecer algo avisando que ele já está comendo

if self.comendo:
    print(f'{self.nome} já está comendo!')
    return
"""
print('Depois da modificação: ')
pessoa_1.comer('carne')

#------------------------------------------------------------------------------------------------------------------
"""
Agora eu preciso fazer ele parar de comer, e com isso criei esse método: 

def parar_comer(self):
    if not self.comendo:
        print(f'{self.nome} não está comendo.')
        return
    print(f'{self.nome} parou de comer!')
    self.comendo = False
"""

pessoa_1.parar_comer()
pessoa_1.parar_comer()
pessoa_1.comer('Arroz')
pessoa_1.parar_comer()
pessoa_1.falar('POO')
pessoa_1.comer('Bolo')
pessoa_1.parar_falar()
pessoa_1.comer('Bolo')
pessoa_1.falar('Estudo')
pessoa_1.parar_comer()
pessoa_1.falar('Estudos')
#------------------------------------------------------------------------------------------------------------------
"""
Terceira Pessoa
"""
pessoa_2.falar('Filmes')
pessoa_2.parar_falar()
pessoa_2.comer('sorvete')
pessoa_1.parar_falar()
pessoa_1.falar('Novos Filmes')
#------------------------------------------------------------------------------------------------------------------
"""
utilizando a variavel que criei pra pegar o ano atual

ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
"""

print(f'\nAno atual!')
print(pessoa_1.ano_atual)
#------------------------------------------------------------------------------------------------------------------
"""
Agora quero saber o ano de nascimento das pessoas 
"""
print(f'Idade da Pessoa 1 :')
print(pessoa_1.pegar_ano_nascimento())
print(f'Idade da Pessoa 2 :')
print(pessoa_2.pegar_ano_nascimento())



