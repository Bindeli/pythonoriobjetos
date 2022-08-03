"""
Formatando valores com modificadores

:s - Texto
:d - inteiros
:f - números ponto flutuante (float)
>. (Número) f - quantidade de casas decimais float
: (Caractere) sendo > ou < ou ^ (Quantidade) (tipo s, d ou f)
< esquerda , > direita, ^ centro
"""

# : caractere quantidade tipo
nome = 'Aneasdson'

# ele vai preencher de #, até ter 30 casas. a direção é onde a variável irá se encontrar.
print(f'{nome:#^30}')
print(f'{nome:#<30}')
print(f'{nome:#>30}')

# lembrando que espaços vazios conta como caractere

# Podemos utilizar o rjust para deixar a variavel na direita e preencher com os caracteres no canto esquerdo
# e o ljust para deixar a variavel no canto esquerdo e preencher com caracteres no canto direito
nome_ljust = nome.ljust(30,'#')
nome_rjust = nome.rjust(30,'#')
print(f'Nome ljust : {nome_ljust}')
print(f'Nome rjust : {nome_rjust}')

# Também podemos transformar todas as letras em minúsculo com a função lower
nome_lower = 'ANEASDSON'
print(f'Transformando todas as letras em minúsculas : {nome_lower.lower()}')
# Ou deixar todas em maiúsculo com a função upper
nome_upper = 'Aneasdon'
print(f'Transformando todas as letras em maiúsculas : {nome_upper.upper()}')
# E também podemos deixar só as primeiras letras em maiúsculo
nome_tittle = 'AneAsDoN RiBeIro'
print(f'Utilizando tittle : {nome_tittle.title()}')

#----------------------------------------------------------------------------------------------------------------------
"""
Indies e Fatiamento de Strings em Python

Cada caracter das strings tem seu indice, lembrando que o primeiro indice começa com 0

EXEMPLO : P y t h o n
          0 1 2 3 4 5 
          
Caso seja negativo para consultar de trás para frente, começa com o último sendo -1 

EXEMPLO : P   y   t   h   o   n
         -6  -5  -4  -3  -2   -1       
Começa com -1 no lado esquerdo, pois o 0 (zero) é de consulta positiva         

Para consultar colocamos a variavel[2]  com as chaves na frente e o indice que queremos consultar, que no caso é 2

Lembrando que espaços vazios conta como caractere e também possuem indices!!!!!!!!!!!!!!!!!!!!!!!!!!

"""
variavel_indice = 'Python'
print(f'\nVariável a ser consultada por indices : {variavel_indice}')
print(f'No indice 3 temos : {variavel_indice[3]}')
print(f'No indice 2 temos : {variavel_indice[2]}')
print(f'No indice 5 temos : {variavel_indice[5]}')
print(f'No indice -1 temos : {variavel_indice[-1]}')
print(f'No indice -3 temos : {variavel_indice[-3]}')
print('')
"""
Agora falando sobre fatiamento : serve para acessar uma parte de string, tendo [inicio:fim:step]

Onde irá começar
Onde irá parar, lembrando que o caracteres com o indice você colocar, não irá aparecer
Step , de quanto a quanto você deseja passar.
"""
variavel_fatiamento = 'Python s2 Aneasdson'
print(f'Variável a ser fatiada: {variavel_fatiamento}')
print(f'Do indice 3 até o indice 8 : {variavel_fatiamento[3:8]}')
print(f'Do indice 4 até o indice 13 : {variavel_fatiamento[4:13]}')
print(f'Desde o começo até o indice 9: {variavel_fatiamento[:9]}')
print(f'Começando deste o indice 9 até o final : {variavel_fatiamento[9:]}') #lembrando que espaço é um caractere
print(f'Agora lendo de dois em dois : {variavel_fatiamento[::2]}')
print(f'A variável ao contrário : {variavel_fatiamento[::-1]}')

#---------------------------------------------------------------------------------------------------------------------
"""
Agora chegando a nossa primeira estrutura de repetição : WHILE

Enquanto uma condição for verdadeira:
    execute o código
    
agora em código

While True:
    código
    
O laço 'while', assim como o 'if' terá um bloco de código 'filho', ou seja, um bloco que será executado abaixo,
dentro da hierarquia.
    
O recomendado para quando for utilizar o laço While, é quando não temos idéia de quando será o final do laço.

Lembrando que para quebrar o laço e não ficar infinitamente, devemos criar uma condição que torne o requisito em False.

Uma boa idéia é utilizar acumulador ou contador!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
#--------
"""
Assim como o pass ou Ellipses, temos o Continue e o Break, que são instruções para o Python

Começando com o 'Continue', é uma instrução para reiniciar um laço, quando o interpretador ler a instrução, ele irá
terminar o laço atual e partir para o próximo laço
"""

"""
Crie um código com while, que imprima na tela uma letra de uma string por vez. 
"""

"""
Com o while, crie uma sequência de 0 até 5, só que não apareça o 3
"""
#---------
"""
Agora falando sobre o Break, é uma instrução para finalizar o loop na hora que o interpretador encontrar-lo. E irá
Saltar para a próxima linha fora do loop

!!!!!
Exemplo : Faça um código que leia uma sequencia de 0 a 6,e pare quando achar o número 3
"""

#--------------------------------------------------------------------------------------------------------------------
"""
Podemos também utilizar Else junto com o While

Que irá rodar, assim que o loop do While terminár, porém se tiver um break, ele irá ignorar o Else, pois faz parte do
loop junto com o While, e irá partir para a próxima linha
"""
print('')
print('Exemplo de While e Else: ')

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1

else:
    print('Cheguei no else.')
print('O print foi executado.')

#--------------------------------------------------------------------------------------------------------------------
"""
Iteração : percorrer sobre um elemento, utilizando loop.
Para iterar sobre um elemento, ele precisa ser iterável, ou seja, deve possuir índices


"""
print('\nExemplo de iteração : ')

"""
Faça um código que tenha uma frase em uma variável com tudo em minúsculo, e devemos iterar sobre essa frase e deixar 
a letra que o usuário escolher em maiúsculo, lembrando que o usuário só pode escrever uma letra, e não pode ser números,
e no final armazene a nova frase em uma nova variável.
"""

# é difícil, então vou te ajudar

#--------------------------------------------------------------------------------------------------------------------













