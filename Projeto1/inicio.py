#print - Comando de saída

print("Olá Mundo")

#input - Comando de entrada
#f - antes das aspas para determinar uma String formatada + {variavel}

nome = input ("Qual seu nome? ")
print(f"Ah, seu nome é {nome}, muito belo!")

#Tipo de Dado - Para determinar o tipo de dado, você o indica e coloca o comando de entrada em parenteses
#Operações - "+,-,/,*" são os simbolos para operações básicas, Soma, Subtração, Divisão e Multiplicação respectivamente.

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

