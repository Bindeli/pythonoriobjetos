"""
Começando com o Print, um comando/função utilizado para exibir uma mensagem na tela para o dev

Onde colocarmos print(e o que desejamos que apareça)

Podendo ser uma variável, uma frase, ...
"""

print('Esta é uma frase executada pelo print')
#__________________________________________________________________________________________________________________
"""
Agora falando sobre o sep = 'separador', é um parâmetro que separada ,pelo elemento dentro das aspas, o argumento
do print

Caso não coloque nada, o padrão é juntar os elementos

Por exemplo : 
"""
print('\nUtilizando o sep:')
print('Anildson','an Ox', sep=' is ')
print('1','2','3', sep='-')
#__________________________________________________________________________________________________________________
"""
End = ''

A função print vem como padrão o end='\n' para saltar uma linha, o valor que vai dentro das aspas, é que irá aparecer
no final do print, e caso você não coloque um \n, não irá ter a quebra de linha e o texto de baixo irá aparecer na
mesma linha de sua mensagem anterior.

Exemplos :
"""

print('\nUtilizando o end:')
print('Esta é a primeira frase e', end='-')
print('agora está é a segunda frase.')

print('An', end='')
print('eas', end='')
print('dson\n')
#__________________________________________________________________________________________________________________
"""
Agora sobre seu funcionamento, podemos utilizar quanto aspas simples e duplas, porém para uma aparecer na tela, devemos
utilizar a outra

"""

print('Uma frase simples porém com "uma parte em destaque" que foi ativada com aspas simples.')
# também podemos utilizando a barra invertida para pedir o python para ignorar a aspas como comando de finalização
print('Outra frase \'com um destaque\' feito com aspas simples porém com algo diferente.\n')
# o mesmo funciona ao contrário

#__________________________________________________________________________________________________________________
"""
Podemos transformar algo em uma string, utilizando a função str, como mostrado abaixo:

E também temos a função type() utilizada para verificar o tipo de dado de um conteúdo
"""
variavel_1 = 123

print(variavel_1, type(variavel_1))
print('Depois da transformação:')
variavel_1 = str(variavel_1)
print(variavel_1, type(variavel_1))
print('')
#__________________________________________________________________________________________________________________
"""
Em Python temos vários tipos de dados:

STR - temos a string, um tipo de texto, dentro de aspas.
INT - um número inteiro, negativo, positivo ou zero, que não tenha casas decimais.
FLOAT - ponto flutuante, positivio, negativo, que tenha algum ponto depois.
BOOL - booleano ou lógico, possuindo apenas dois valores, em outras linguagens é 1 e 0, porém em Python, temos os valores
True e False, para checar a lógica do código, retornando algo entre os dois, verdadeiro ou falso
"""
joao = 'João'
numero_string = '1'
numero_ex1 = 1
numero_float = 10.5

print(f'{joao} será visto como string : {type(joao)}')
print(f'{numero_string} será visto como string, pois está dentro de aspas : {type(numero_string)}')
print(f'{numero_ex1} é um número inteiro: {type(numero_ex1)}')
print(f'{numero_float} é um número de ponto flutuante ou float: {type(numero_float)}')
print(f'Agora checando por boolean se 10==10 : {type(10==10)}')
print(f"Agora checando por boolean se l é igual a L: {type('l'=='L')}")
print(f'Vai dar False, pois uma letra está em minúsculo e a outra em maiúscula, no Python, não é visto como igual.\n')
#__________________________________________________________________________________________________________________
print(f'Operadores Aritméticos:')
"""
Agora falando sobre os operadores aritméticos, temos primeiro a adição +, como na matemática, utilizada para soma
Porém em Python, caso for uma string, serve para concatenação também
"""
print(f'Soma 5 + 5: {5+5}')
print(f"Concatenação de string : {'5'+'5'} ")
# Temos também a Subtração -
print(f'Subtração 10 - 5: {10-5}')
"""
Temos também a multiplicação * , como na matemática para multiplicar valores
E também em python, podemos multiplicar/repetir strings
"""
print(f'Multiplicação 5 * 5 : {5*5}')
print(f"Multiplicação/Repetição de String: {'str-'*5} ")

# Temos a divisão que retorna um valor float
print(f'Divisão 10 / 3 : {10/3}')

# Temos a divisão inteira que retorna um valor arredondado
print(f'Divisão inteira que retorna um valor arredondado 10//3 : {10//3}')

# Temos também a Potenciação ou Exponenciação:
print(f'Potenciação ou Exponenciação 2 ** 4 : {2 ** 4}')

# Temos também o Resto da divisão %, que retorna o que sobrou da divisão, 10/3 vai restar 1, enquanto 10/5 vai restar 0
print(f'Resto da divisão % que retorna literalmente o resto: ')
print(f'10 % 3 : {10 % 3}')
print(f'10 % 5 : {10 % 5}\n')
#__________________________________________________________________________________________________________________
"""
Agora falando sobre Variáveis : São elementos que guardam um valor dentro de si, podendo ser uma string, inteiro, float,
boolean, algum dado específico, podendo ser até utilizando para comparação.

Para atribuir um valor a uma variável, utilizando o igual único = 

variavel = valor
variavel_1 = valor

De começo vamos utilizar apenas letras minúsculas para criação de variáveis
"""
print(f'Variáveis : ')
nome = 'Maria'
idade = 25
altura = 1.70
peso = 70

# E devemos chamar a variável no print para aparecer seu valor :

print(f'Nome : {nome}')
print(f'Idade : {idade}')
print(f'Altura : {altura}')
print(f'Peso : {idade}')

# Utilizando seus dados , descubra o ano de nascimento de Maria e seu imc = peso / altura ** 2 exibindo em somente
# uma linha de print

print('')
#__________________________________________________________________________________________________________________
"""
Agora falando sobre a função Input, sua utilidade é para que o código solicite ao usuário que dê entrada com algum dado
ou valor, criamos uma variável para receber o valor inserido pelo usuário.

variavel = input('Escreva algo: ')

Lembrando !!!!! O dado inserido é sempre transformado em uma string, então se estiver precisando de um dado numérico,
lembre-se de transformar-los em inteiro com a função int(), ou float com a função float()
"""

# Abaixo Vamos criar um modelo igual do exemplo anterior, o usuário deve entrar com seu nome, idade, peso, altura,
# para que o código criado leia e mostre seu ano de nascimento e seu imc.

# crie em um outro arquivo para facilitar rsrsrs

#__________________________________________________________________________________________________________________
"""
Agora falando sobre condições IF, ELIF E ELSE!!!

São estruturas condicionais, que irá verificar uma determinada expressão e se a expressão atender ao requisito, ela 
irá rodar o código inserido dentro de uma dessas 3 funções.

If é o comando inicial, podendo ser utilizada sozinha também, não depende da elif e else para funcionar.

if (expressão_for_verdadeira):
    executar_bloco_de_codigo()
    
Else é um comando utilizado para executar um bloco de código caso nenhuma das condições atender ao requisito

if (expressão_for_verdadeira):
    executar_primeiro_bloco_de_codigo()
else:
    executar_segundo_bloco_de_codigo()
    
Agora ELIF, é utilizado quando queremos realizar uma verificação de outras expressões além do if e else

Else e elif são dependentes do IF para funcionar.

if expressão:
    código
elif expressão:
    código
elif expressão:
    código
elif expressão:
    código
else:
    código
"""

#__________________________________________________________________________________________________________________
"""
Agora falando sobre Operadores relacionais : tem a principal função de comparação, entre elementos dentro do código.
Retornando um valor boolean True ou False

== Igual-igual , se um valor é igual ao outro, podendo ser string ou um valor numerico
2 == 2 ? True , c == C ? False

> temos o maior que, se um valor é maior que o outro, ele retornará true ou false
>= maior ou igual a que
< menor que
<= menor ou igual a 
!= Diferente, verificando se um valor é diferente de um outro valor
"""
#__________________________________________________________________________________________________________________
"""
1 - Utilizando o que você aprendeu sobre Input e as estruturas condicionais, faça um código que verifique se o número
é par ou impar.

2 - Utilizando o input e os comandos condicionais, peça ao usuário para digitar o nome, e depois a idade, e verifique se
é uma criança, um adolescente ou um adulto. Imprima uma mensagem com o nome e a categoria a qual ele pertence.
"""
print('')

# Tenhos mais exemplos na minha lista de atividade!! Lembrar!
#__________________________________________________________________________________________________________________
"""
Agora falando sobre Operadores Lógicos 

and , verificando se um valor E um outro valor seguem uma condição!!! os dois devem ser verdadeiros
verdadeiro e verdadeiro = verdadeiro
verdadeiro e falso = falso

if a == a and b == b:
    execute esse código
    
-----------------------------------------------------------------------------------------------------------------
or , se um dos dois for Verdadeiro, ele irá executar o código
if a == A or b == b:
    irá executar esse código pois b == b
    
-----------------------------------------------------------------------------------------------------------------
not , uma verificação ao contrário, se algo não for isso, execute o código

if not 2 < 1:
    vai executar o código pois 2 é maior que 1
    
-----------------------------------------------------------------------------------------------------------------
in, verificar se algo se encontra em alguma coisa, um exemplo famoso é verificar se uma letra pertece a um nome

if 'L' in 'Lucas':
    vai executar pois o L maiúsculo se encontra no nome
-----------------------------------------------------------------------------------------------------------------
not in, o contrário de in, se algo não se encontra em alguma coisa, vai executar.
bem mais utilizável que se possa imagina, normalmente utilizado no primeiro if para confirmar se realmente não está.

if 'l' not in 'Lucas':
    vai executar pois o l minúsculo não se encontra no nome
"""

# Como um exemplo para esse conteúdo, crie uma senha de sistema bem muito altamente simples, e pela para o usuário
# digitar o usuário e sua senha, caso bater com o usuário e senha cadastrados, imprima na tela confirmando o sucesso
print('')
#__________________________________________________________________________________________________________________
"""
A função Len : a função len serve para contar a quantidade de caracteres ou elementos que temos dentro de algo.
Inicialmente vamos utilizar para ver quantos caracteres temos em uma string.

Um bom exemplo é um login simples, onde o usuário ou senha deve conter um total máximo ou mínimo de dígitos.

Não utilizamos para valores números como float ou int.

Porém a função LEN retorna um valor inteiro e pode ser utilizado para cálculos.

Exemplo:  len(variavel)

"""

"""
Faça um código que peça ao usuário dar de entrada com dados para um login e com senha

O login deve conter no mínimo 8 dígitos e a senha deve conter no mínimo 6 dígitos com um caracter especial que é o @

Caso passe por esses condições, armazene os dois valores em dois variáveis representando o login e senha oficial.
"""

"""
Faça um programa que peça o primeiro nome do usuário;
Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto.";
Se tiver entre 5 a 6 letras, escreva: "Seu nome é normal."
Maior que 6, escreva: "Seu nome é muito grande."
"""

"""
Faça um programa que pergunte a hora ao usuário;
Baseando-se no horário descrito, exiba a saudação apropriada:
Ex: Bom dia de 0-11   Boa tarde de 12 - 17   Boa noite de 18-23
Caso o usuário não digite um valor válido, informe que ele não digitou um valor válido.
"""

#__________________________________________________________________________________________________________________
"""
PASS Ee Elipses 

utilizamos esses 2 recursos para guardar um espaço no código que irá ser modificado posteriormente, evitando erros
na hora de executar o código.

if condição:
    pass
else:
    código
    
ou Elipses que é representado por 3 pontos ...

if condição:
    ...
else:
    código
"""
#__________________________________________________________________________________________________________________

"""
Agora para finalizar o Resumo 1 com chave de ouro : Funções de checagem 

isnumeric
isdigit
isdecimal

Utilizadas para verificar se uma string contém somente números e se pode ser modificada para inteiro
Float mesmo sendo um número, não é considerado como aceitável por estas funções

if numero_1 isdigit():
    execute o código.
"""

"""
Faça uma calculadora que pela ao usuário dois números, depois verifique se são dígitos válidos ou não, a seguir,
peça para ele escolher um tipo de operação entre soma, subtração, divisão, multiplicação

Importante para esse exercício é impedir erros, então verifique cada ação com um pensamento "e se ele digitar isso..."
"""

#__________________________________________________________________________________________________________________