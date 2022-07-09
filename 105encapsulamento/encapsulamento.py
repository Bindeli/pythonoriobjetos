"""
AULA 105 - Encapsulamento

Utilizado para esconder certas partes do seu código para proteger sua aplicação, Classe em sí

Modificadores de acesso - método e atributos public, protected, private.

public - são métodos e atributos que podem ser acessados dentro e fora da classe
protected - são métodos e atributos que podem ser acessados apenas dentro da classe ou das filhas daquela classe
private - só está disponível dentro da classe

_ privado/protected (public _) , só que de maneira mais fraca, mais sútil, podendo acessar mesmo assim só digitando o _atributo
__ privado, vai proibir que acesse o atributo, podendo também ser utilizado para os métodos
porém este último posso acessar utilizando _NOMEDACLASSE__ATRIBUTO

def __inserir(self):
"""

class BaseDeDados:
    def __init__(self, ): # um tipo de construtor
        # antes ela estava assim : self.dados = {}
        self.__dados = {}
        # pela lógica do python, se você tiver um _ antes, recomendasse que não acesse o atributo

    @property #aqui eu quero obter um dado, fazendo um método da classe parecer um atributo da classe
    def dados(self):
        return self.__dados

    def inserir_cliente(self,id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

base_dados_1 = BaseDeDados()
base_dados_1.inserir_cliente(1, 'Lucas')
base_dados_1.inserir_cliente(2, 'Nilneas')
base_dados_1.inserir_cliente(3, 'Marcelo')
base_dados_1.inserir_cliente(4, 'Almirante')
base_dados_1.inserir_cliente(5, 'Eduardo')
base_dados_1.__dados = 'Outra coisa'
print(base_dados_1.__dados) # será um outro atributo que não está ligado com o coração de minha classe
print(base_dados_1._BaseDeDados__dados)

# base_dados_1.apaga_cliente(4)
# print('Após utilizar o método apaga cliente no 4:')
# base_dados_1.lista_clientes()

# self.dados = {} # esse é o coração de minha classe, ele é público, ele está acessível dentro e fora da classe

#_____________________________________________________________________________________________________________________
"""
se eu mandasse um, por exemplo:

base_dados_1.dados = 'Recebesse isso'

Eu iria quebrar todo o meu código. O atributo principal da minha classe é público, e se por um motivo
eu ou outro desenvolvedor mudar o valor desse atributo, a classe é interamente quebrada.

É Normal então utilizar um atributo privado ou protected para esse tipo de atributo

pela lógica do python, se você tiver um _ antes, recomendasse que não acesse o atributo

Então vamos colocar um _ antes de nosso atributo principal

E logo depois, podemos perceber que ele não irá aparecer mais na lista para completar o código ao chamar-lo

Porém mesmo com o _atributo, ainda podemos acessar-lo e quebrar o código chamando desta maneira :

base_dados_1._dados = 'Recebesse isso'

Então o ideal é utilizar um mais forte, que recomenda fortemente que não seja acessado

que no caso, é utilizando dois __atributo

porém se eu colocar um base_dados_1.__dados = 'Recebesse isso'

O python irá utilizar um recurso que ele renomea utilizando o nome da classe, criando um novo

E caso eu queira ver o atributo fora da classe, eu terei que escrever desta maneira :

print(base_dados_1._BaseDeDados__dados)

"""
#_____________________________________________________________________________________________________________________

# Caso eu queira liberar o acesso do atributo aos valores da variável, posso utilizar o getter e setter
print(f'Após utilizar getter e setter :')
print(base_dados_1.dados)
# porém ainda não criamos um setter para modificar valores como base_dados_1.__dados = 'Recebesse isso'
#_____________________________________________________________________________________________________________________
base_dados_1.lista_clientes()
base_dados_1.apaga_cliente(4)
print(f'Após excluir o 4: ')
base_dados_1.lista_clientes()
#_____________________________________________________________________________________________________________________