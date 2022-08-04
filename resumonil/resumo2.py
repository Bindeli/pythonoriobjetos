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
e no final armazene a nova frase em uma nova variável. Dica : tamanho da frase.
"""

# é difícil, então vou te ajudar

#--------------------------------------------------------------------------------------------------------------------
"""
Repetição com For In

Já o laço For serve para iterar em estruturas onde sabemos o seu fim.

Exemplo de utilização :

texto = 'Python'

for letra in texto:
    print(letra)
    
esse código vai imprimir uma letra a cada laço da variável "texto"

Aqui também podemos utilizar o break para terminar o laço ou o continue para pular para o próximo laço!!!!!

"""

# Utilizar um debugger para mostrar

palavra_teste = 'Ha57gda67g'

for letra in palavra_teste:
    if letra.isdigit():
        print(f'Esse letra é um dígito : {letra} {type(letra)}', end='')
        int(letra)
        print(f', Agora a letra é {type(letra)}')
    else:
        print(f'Letra: {letra}')
print('')

#--------------------------------------------------------------------------------------------------
"""
Range em Python : é uma função que irá retornar um conjunto de números sequencias setadas pelo usuário.

Por exemplo um range(10) irá ter os valores 0,1,2,3,4,5,6,7,8,9.

lista = list(range(10))
print(f'{lista}') saída : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Assim como o fatiamento, no range teremos um ponto de inicio, de parada e de step

Exemplo: 

range(2, 15, 2) = saída : [2, 4, 6, 8, 10, 12, 14]

lista2 = list(range(2,15,2))
print(f'{lista2}')

"""
#
"""
Com a função for in junto com range, crie um código que leia uma sequencia de números pulando de 3 em 3.
"""
#
"""
Crie um código que mostre os múltiplos de 7, de 0 até 100.
"""
#
"""
Crie um código que pegue uma palavra e transforme as vogais em @ e mude as consoantes em letras maísculas.
"""
#

#------------------------------------------------------------------------------------------------------------
"""
Lista em Python!!!!!!!!!!!!!!!!!!

lista é um tipo de dado para armazenar multiplos valores nela. Enquanto a variavel comum que armazena apenas um valor

lista_exemplo = ['Anildson','s2','Eneas','casalzinho',10, 8,5, True] 

Esse é uma lista que iniciamo com [], pode armazenar elementos Strings, inteiros, float, e boolean!

E para acessar esse valores podemos utilizar os índices!!!!!!

          0   1   2   3   4  
lista = ['A','B','C','D','E']
         -5  -4  -3  -2  -1

Lembrando que a lista é um elemento mutável, ou seja, podemos modificar um valor dentro dela.

Podemos consultar por índices:

lista[2] = C

Podemos utilizar o fatiamento

lista[0:4:2] = A C

"""
#--------------------------------------------------------------------------------------------------
"""
Funções de Listas:

Começando por extend = mescla duas listas, fazendo com que passe a existir apenas uma, com todos os elementos

lista_1 = [1,2,3]
lista_2 = [4,5,6]

lista_final = [1,2,3,4,5,6]
"""
#
"""
Utilizando o extende, junte essas duas listas :
lista 1 = ['a','d',3,10.5]
lista 2 = [10,'anea','sd', 98]
"""

#--------------------------------------------------------------------------------------------------
"""
Função Append = insere um registro como último elemento, quando desejamos adicionar um elemento na lista

lista = [1,2,3]

lista.append(4)

lista = [1,2,3,4]
"""
#
"""
Faça um código que adicione em uma lista, apenas números pares na sequencia de 0 a 20
"""
#--------------------------------------------------------------------------------------------------
"""
Insert = Quando desejamos adicionar um elemento em determinada posição que indicarmos.

lista_ex = [0,1,2,3]

lista_ex.insert(2,'testando') # Saída [0, 1, 'testando', 2, 3]

print(lista_ex)

"""
#--------------------------------------------------------------------------------------------------
"""
Função Pop() - Ela remove o último elemento da lista (caso o índice não seja indicamos em parênteses)

lista = [0,1,2,3,4,5]

lista.pop()

lista = [0,1,2,3,4]
"""
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


