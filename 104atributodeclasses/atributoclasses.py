"""
AULA 104 - Atributos de Classe - Python Orientado a Objetos

"""

class Classe:
    variavel = 123
    # essa variável não é de instâncias dessa classe, ela na verdade é uma variável da classe




# essa variável não é de instâncias dessa classe, ela na verdade é uma variável da classe
# Porém eu posso imprimir a variavel utilizando a instância
valor_a = Classe()
valor_b = Classe()

print(f'Valor de A : {valor_a.variavel}')
print(f'Valor de B : {valor_b.variavel}')

# Ela estará disponível para todas as instâncias da classe
# e também posso chamar ela direto para o print

print(f'Valor na classe : {Classe.variavel}')
#-------------------------------------------------------------------------------------------------------------------
# Posso mudar também o valor de uma instância em um elemento , como por exemplo :

valor_a.variavel = 321
print(f'\nDepois de mudar somente no valor A : ')
print(f'Valor de A : {valor_a.variavel}')
print(f'Valor de B : {valor_b.variavel}')
print(f'Valor na classe : {Classe.variavel}')

# utilizando o __dict__ para verificar o conteúdo de a

print(f'Transformando o A em diciopnário para verificar seus valores :')
print(f'A : {valor_a.__dict__}')
print(f'Transformando o B em diciopnário para verificar seus valores :')
print(f'B : {valor_b.__dict__}')

"""
Quando você executa executa isso aqui "valor_a.Classe" direto da instância, o interpretador do python
Irá verificar na instância em si se a Classe existe, se ela existir, ele já vai exibir o valor dela

Se ela não existir na instância, ele vai procurar no classe em si

Quando eu faço isso aqui : valor_a.variavel = 321, eu não estou alterando o valor da variavel da classe
E sim estou criando um atributo direto na minha instância "valor_a"
"""


#-------------------------------------------------------------------------------------------------------------------
# Porém se eu falar que

Classe.variavel = 321

# vai mudar para todas as instância que utilizemos

print(f'\nDepois de mudar o valor da instância : ')
print(f'Valor de A : {valor_a.variavel}')
print(f'Valor de B : {valor_b.variavel}')
print(f'Valor na classe : {Classe.variavel}')

#-------------------------------------------------------------------------------------------------------------------
# Um outro exemplo que podemos utilizar é quando dar conflito em algum nome

# Então vamos criar uma função def __init__

class OutraClasse:
    numero = 123

    def __init__(self):  # self é uma variavel de instância e o numero é uma variável de classe
        self.numero = 321

# Se eu tenho duas instâncias que estão sendo inicializadas, e as duas instâncias terão o valor 321
# já quando eu chamar diretamente pela classe, terá o valor normal do numero 123

variavel_1 = OutraClasse()
variavel_2 = OutraClasse()
print(f'\nOutro Exemplo:')
print(f'Variável 1 : {variavel_1.numero}')
print(f'Variável 2 : {variavel_2.numero}')
print(f'Valor da variável da Classe: {OutraClasse.numero}')

#-------------------------------------------------------------------------------------------------------------------

