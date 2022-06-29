#Para criar classe eu Python, eu utilizo a função classe e o nome eu começo com letra maiúscula

from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) # variavel da classe em si, que pega o ano atual
    # cada pessoa vai ter um nome, idade, comportamento.
    # Aqui vamos criar um método especial
    # def falar(self): # o parâmetro self está ligado a instância ligado a ela, no caso pessoa_1 ou pessoa_2
    #     # como se fosse, pessoa_1.falar(pessoa_1)
    #     print("Fala da pessoa...")
    def __init__(self, nome, idade, comendo=False, falando=False): # criando um construtor
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        algum_valor = 'valor'
        print(algum_valor)

    """
    def outro_metodo(self):
        # eu não consigo puxar a variavel 'algum_valor' criada pra ca
        # mas posso chamar, por exemplo, nome e idade e as outras duas
        print(self.nome) # que não apresenta erro
    """

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo!')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}!')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        if self.falando:
            print(f'{self.nome} está falando e não pode comer ao mesmo tempo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer!')
        self.comendo = False
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
        print(f'{self.nome} parou de falar.')
        self.falando = False
    def pegar_ano_nascimento(self):
        return self.ano_atual - self.idade

"""
Um método é uma função que pertence a uma classe
"""

# Se fosse um nome composto, tipo BasePessoa, as duas primeiras letras de cada, ficaria em maiúsculo