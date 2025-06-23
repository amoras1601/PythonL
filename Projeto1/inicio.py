#print - Comando de saída

print("Olá Mundo")

#input - Comando de entrada
#f - antes das aspas para determinar uma String formatada + {variavel}

nome = input ("Qual seu nome? ")
print(f"Ah, seu nome é {nome}, muito belo!")

#Tipo de Dado - Para determinar o tipo de dado, você o indica e coloca o comando de entrada em parenteses
#Operações - "+,-,/,*" são os simbolos para operações básicas, Soma, Subtração, Divisão e Multiplicação respectivamente.
#Há outros, veja:
#Exponenciação - 
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Divisão Arredonda -
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(9.1 // 3.)

#Restante (módulo) - O resultado do operador é o restante após a divisão do número inteiro. 14 / 4 == 3 (inteiro menor) e sobra 2 ----- 14 % 4 == 2

print(14 % 4)

#Int - Valor inteiro, sem ponto flutuante, ou seja 4 != 4.0 (quatro diferente de quatro ponto 0) visto que "." torna o valor float.

n1 = int (input("digite um número: "))
n2 = int (input("digite um número novamente: "))
soma = n1 + n2
sub = n1 - n2
print (f"a soma dos números que você digitou é {soma} e a subtração é {sub}")

#Float - Tipo de dado de ponto flutuante (ex: 5.5 , 4.0 - Perceba que o numero cinco e meio foi escrito com um ponto, 
#Python não aceita virgula para adcionar decimais.). Se caso o valor de entrada seja colocado com virgúla
#por hora ele apresentará: ValueError: could not convert string to float: '20,6'

nFloat1 = float(input("digite um número de ponto flutuante: "))
nFloat2 = float(input("digite um número de ponto flutuante qualquer novamente: "))
print(f"A soma dos seus numeros é", nFloat1 + nFloat2)

#Há ainda a operação de potência, para notação científica, ultilzamos o e ou E, por exemplo: 3E8 é o mesmo que 3x10^8 (3 vezes 10 á oitava)
print(3e8)

#Strings - basicamente, python reconhece como texto aquilo que é colocado entre aspas. Por exemplo: 
print("Eu sou uma String")

#Para colocar uma palavra entre aspas dentro de uma string, usamos a barra invertida \ (alt 92) Pois sabemos que ela mostra o escape do comando
#Por exemplo:
print("Eu sou uma \"Mensagem\"")
print("I\'m \"Monty Python\"") 
#Ou
print("")
#Ou então, aspas duplas entre aspas simples, assim:
print('Ola "Mundo"')

#Valores Booleanos - verificam a veracidade da coisa - Python é binário e trabalha com apenas dois valores de veracidade, True e False respectivamente 1 e 0.
#Sim isso é verdade; Ou Não, isso é falso. Sempre.

#Variáveis - caixas em forma de dados
#o nome da variável deve ser composto de letras maiúsculas ou minúsculas, dígitos e o caractere _ (sublinhado)
#o nome da variável deve começar com uma letra;
#o caractere de sublinhado é uma letra;
#as letras maiúsculas e minúsculas são tratadas como diferentes (um pouco diferente do que no mundo real - Alice e ALICE são os mesmos nomes, mas em Python são dois nomes de variáveis diferentes e, consequentemente, duas variáveis diferentes);
#o nome da variável não deve ser nenhuma das palavras reservadas do Python (as palavras-chave - explicaremos mais sobre isso em breve).

#Palavras reservadas
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
# 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Criação de variáveis
