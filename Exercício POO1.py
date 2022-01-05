texto = 'pratica 1'
calculo = 9
dinheiro = float(9.99)

print(type(texto))
print(type(calculo))
print(type(dinheiro))

#Desafio dois faça um comentário, sério só isso

'''comentário de mais d uma linha é 3 aspas simples
Testando e aprendendo'''

#crie uma variável nome e o conteudo dela seja algo digitado pelo usuário

nome = input('Digite seu nome: ')
print(f'Olá {nome}, seja bem vindo!!!')

#Exiba em tela o conteúdo e o tipo da variável "num1"

num1 = 1996

print(num1)
print(type(num1))

#Peça para que o usuário digite um número e exiba no console o numero digitado

num2 = input("Digite um número: ")
print(f'Seu número digitado é: {num2}')


#Some os resultados das variáveis num3 e num4 e exiba seus valores

num3, num4 = 156, 100

soma = num3 + num4
print(num3 + num4)
print(soma)

#multiplique os valores das variáveis

print(num4 * num3)

#Eleve um número a sua oitava potencia exibindo seu valor em tela

print(num3 ** 8)

#verifique se a var1 é maior q a var2

var1 = 123
var2 = 58

print(var1 > var2)

#verifique se var1 e var2 são equivalentes

print(var1 == var2)

#verifique se var1 e var2 são diferentes

print(var1 != var2)

#verifique se a variável é menor ou igual a 100

print(var2 <= 100)

#verifique se os valores de var1 e var2 são menores que 100

print(var1 <= 100 and var2 <= 100)

#verifique se o valor de numl1 consta dentro da lista

numl1 = 100

lista1 = [10, 100, 1000, 10000, 100000]

print(numl1 in lista1)

'''crie duas variáveis com dois valores numéricos, caso o valor da primeira seja maior que o da segunda,
exiba em tela essa resposta, caso contrário, exiba em tela seu valor é menor.'''
 
varN1 = 25
varN2 = 26

if varN1 > varN2:
    print("Variável 1 mario que variável 2")
else:
    print('Variável 1 menor que variável 2')

#Peça para que o usuário digite um número, em seguida retorne uma mensaguem dizendo se tal número é par ou impar

impar = int(input('Digite um número: '))

if (impar % 2 ) == 0:
    print(f'{impar} é par')
else:
    print(f'{impar} é impar')

'''Crie uma variável com valor inicial 0, enquanto o valor dessa variável for menor que 10, exiba em tela
o próprio valor da variável, a cada execução a mesma deve ter seu valor atualizado, acrescido de uma unidade'''

varwhile = 0

while varwhile <=10:
    print(varwhile)
    varwhile += 1

'''Crie um laço de repetição que percorre cada elemento da string "Nikola Tesla", exibindo cada elemento
individualmente em tela'''

varTexto = "Nikola Tesla"

for n in varTexto:
    print(n)

'''Crie uma lista com 5 elementos, em seguida crie uma laço de repetição que percorra cada elemneto dessa lista,
exibindo individualmente cada um em tela.'''

lista10 = ['Água', 'Arroz', 'Pão', 'Leite', 'Massa']

for n in lista10:
    print(n)

'''Crie um programa que lê um valor de início e um valor de fim, exibindo em tela a contagem dos números nesse
intervalo'''

inicio = int(input('Digite o número de início da contagem: '))
fim = int(input('Digite o número final da contagem: '))

while inicio <= fim:
    print(inicio)
    inicio += 1

'''Resposta otimizada da aula
for i in range(inicio, fim+1):
    print(i)'''

'''Crie um programa que realize a contagem de 0 a 50, exibindo apenas os números pares'''

for n in range (0, 51):
    if (n % 2) == 0:
        print(n)

'''Crie um programa que realiza progressão aritimética de 20 elementos, com primeiro termo e razão
definidos pelo usuário'''

n = 0
numT1 = int(input("Digite o primeiro termo da progressão: "))
numR1 = int(input('Digite o numero razão da progressão: '))

while n < 20:
    print(numT1)
    numT1 = numT1 + numR1
    n += 1

'''Realize a criação de uma simples tabuada que é exibida em tela para o usuário'''

x = int(input("Digite um número: "))

for num in range (1,11):
    print(f'{x} X {num} = {x * num}')