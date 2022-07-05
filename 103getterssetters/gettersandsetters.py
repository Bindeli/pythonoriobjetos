"""
103 - @property - Getters e Setters - Python Orientado a Objetos
"""

"""
Para essa aula, vamos criar um exemplo e mostrar solução para o exemplo
"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco- (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A','@').capitalize() # só a primeira letra maiúscula
        # lembrando que devemos puxar com o _


    # Getter - vai receber o valor, e ele deve rodar antes do construtor __init__
    @property # lembrando que isso é um decorador
    def preco(self):
        # esse método vai chamar o mesmo nome da variável que dá o atributo preço
        return self._preco

    # Setter - ele vai configurar o meu preço
    @preco.setter # vai ser @ e o nome da propriedade que eu quero e .setter
    def preco(self, valor): # o valor vai ser atributo para a variável de cima
        # agora para validar, utilizando o isinstance, verificando um valor e em seguida se é uma instância de string
        # lembrando que str é uma classe em python
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preco = valor
        # lembrando que devemos puxar com o _


produto_1 = Produto('Camisa', 50)
produto_1.desconto(10)
print(f'Produto {produto_1.nome} : com o desconto, o valor passa a ser : {produto_1.preco}')

produto_2 = Produto('CaNeCa', 20)
produto_2.desconto(20)
print(f'Produto {produto_2.nome} : com o desconto, o valor passa a ser : {produto_2.preco}')

produto_3 = Produto('BERMUDA', 'R$30') # exemplo de erro
produto_3.desconto(10)
print(f'Produto {produto_3.nome} : com o desconto, o valor passa a ser : {produto_3.preco}')

#-------------------------------------------------------------------------------------------------------------------

"""
Por acaso, se houver alteração no código e alguém alterar o valor int ou float para uma string 
como por exemplo , 'R$15'

Eu iria precisar filtrar o preço, antes de realizar esta linha : self.preco = preco
Pois o construtor já recebe um valor logo de cara e configura o valor do preço

Supondo que eu já tenha várias linhas de código já configuradas, e para não alterar tudo

Posso utilizar os dois, Getters 'de receber algo' e Setters 'de modificar algo'

Com o Getter e o Setter, primeiro irá passar pelos dois e depois irá para o construtor

Eles são uma proteção para o atributo

Porém no exemplo, iria dar problema se tivesse algo como espaço, ponto, vírgula ou algo a mais

E poderiamos arrumar com expressões regulares, que irei ver mais a frente do curso
"""