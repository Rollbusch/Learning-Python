num1 = int(input('Primeiro número : '))
num2 = int(input('Segundo número : '))
num3 = int(input('Terceiro número : '))
# Variáveis 
menor = num1
maior = num1
# Verificando quem é o menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3
# Verificando quem é o maior
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3
# Printando na tela
print('Menor: ', menor)
print('Maior: ', maior)