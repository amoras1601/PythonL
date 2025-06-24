#Loops
#Loops se leem da seguinte forma, Enquanto isso acontecer. Faça isso;  Se isso Acontecer, Faça isso.

#Loops infinitos - Quando algo é ordenado a acontecer enquanto algo imutavel acontecer. Por exemplo:

#   while True:
#       print("Estou preso dentro de um loop.")
# Ou então
#   while 1>0:
#       print("Estou preso dentro de um loop.")
# Como 1 sempre vai ser maior que zero, esse loop é interminavel, e ficaria ativo infinitamente.


#Loops Dependentes - Que dependem de algo para terminar. Como o loop é lido da seguinte forma: Enquanto isso acontecer, faça isso. significa que se deixar de acontecer, ele acaba.
#Por Exemplo:
print("----------------------------------------------------------")
# Armazene o maior número atual aqui.
Maior_Numero = -999999999
 
# Insira o primeiro valor.
numero = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while numero != -1:
    # O número é maior que o maior_número?
    if numero > Maior_Numero:
        # Sim, atualize o maior_número.
        Maior_Numero = numero
    # Insira o próximo número.
    numero = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", Maior_Numero)

#Mais um exemplo simples
print("----------------------------------------------------------")
# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
numeros_impares = 0
numeros_pares = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        numeros_impares += 1
    else:
        # Aumente o contador even_numbers.
        numeros_pares += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares contam:", numeros_impares)
print("Números pares contam:", numeros_pares)

#counter - É o i para o JAVA, enquanto counter for diferente de um valor, faça isso, e opere em direção ao valor de counter, assim,
# o loop terá um limite. Nesse caso, counter é maior, e vai em direção á o valor zero, de um em um.
print("----------------------------------------------------------")
counter = 5
while counter != 0: #aqui "conter:" recebe a mesma funcionalidade
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)
 
#For - tambem é uma estrutura de repetição. As vezes é melhor contar quantas vezes o loop aconteceu, 
#do que verdadeiramente o fator que leva ele á acontecer

#imagine, se esse codigo fosse ultilizado:
#i = 0
#while i < 100:
    # faça_algo()
    # i += 1

#imagina ter que contar quantas vezes isso rolou? uma estrutura de repetição é capaz de contar, e no caso, é o For

for i in range(10):
   print("O valor de i é atualmente", i)

#Difetente do java, n é necessario especificar que i somará 1 á ele mesmo. 
#Mas assim como java, o contador se inicia no zero, e portanto o exemplo acima terminará em 9
#range mostra quantas vezes o loop deve ser executado.

#Porém, é possivel sim, especificar aquilo que não foi colocado. 
#Por exemplo:

for i in range(1,11):
   print(i)

#assim iniciará em 1 e irá ate 10.

#iteradores - Range criou um iterador, que é um objeto do python, que permite que criemos uma sequência com ele
#É possivel vizualizar iteradores nas listas, ou strings


#Quando usar? - 
#While é ultilizado quando não se sabe exatamente quantas vezes a sessão irá acontecer
#for é ultilizado quando se tem uma noção

#Break - Quebra o looping

while True:
    numero = int(input("Digite um numero par: "))
    if numero % 2 == 0:
        print("Obrigado!")
        break
    else:
        print("Mano essa é a droga de um numero impar mano")

print("Fim do programa mano")

#Continue - Quando pfoge da condição do if, para ir ao else, o continue faz voltar e pular para o proximo.
#Exemplo com listas

numeros = [5,3,2,4,8,6,9]
for n in numeros:
    if n % 2 != 0:
        continue
    print(f"o numero {n} é par")
        
#Iterando Dicionários

dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for c, v in dados.items():
    print(f"{c}:{v}")

#se caso só valores

dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for v in dados.values():
    print(f"{v}")

#se caso só chaves
dados = {"nome":"gustavo","inscritos":12,"categoria":"gostosuras"}

for c in dados.keys():
    print(f"{c}")

#Desafios: 
#1 - Imprima os numeros de 1 a 10 usando while
#2 - Crie um simulador de tabuada, recebe um numero e exibe a tabuada dele
#3 - Escreva um programa que conta quantas vogais tem na palavra
#4 - Escreva um programa onde o sistema exibe uma tabuada de 1 a 100

