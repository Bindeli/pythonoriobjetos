from random import randint

class Pessoa:
    ano_atual = 2022 # atributo de classe

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # para chamar esse método, eu preciso passar uma instância, que é self
        print(self.ano_atual - self.idade)


    @classmethod # eu não preciso da instância, mas eu preciso da classe em sí
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


    @staticmethod # Não precisa da instância e nem da classe
    def gera_id():
        # podemos criar variáveis sem cls e sem self aqui, não podemos utilizar os dois
        # porém a variável só vai estar disponível dentro deste método

        rand = randint(10000, 19999) # vai de 10mil até 19mil999
        return rand


"""
o staticmethod é um método que você não vai utilizar a classe em si e nem a instância, seria como uma função
normal, fora da classe, porém essa função por questão de organização, deveria estar dentro da minha classe

Vamos utilizar como exemplo, uma função que gere id de uma pessoa
Por exemplo, para ficar salvo na base de dados ou para fazer algo com a identificação

Podemos perceber que o método estático não recebe classe e nem instância

Posso receber os parâmetros que eu quiser colocar

#--------------------------------------------------

Vamos dar um import no módulo random para criar um id para a pessoa.
quero que gere um número aleatório que tenha 4 dígitos

"""
pessoa_1 = Pessoa('Lucas', 25)
print(pessoa_1)
print(pessoa_1.nome, pessoa_1.idade)
pessoa_1.get_ano_nascimento()
print(f'O ID de {pessoa_1.nome} é {pessoa_1.gera_id()}')
# e também posso chamar pela instância
print(pessoa_1.gera_id())

"""
Podemos utilizar uma instância ou classe para chamar o método estático, porém dentro dele, não podemos utilizar
nem self e nem a classe
"""
