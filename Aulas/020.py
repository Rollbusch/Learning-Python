import random # importa a biblioteca random

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista) # .shuffle() embaralha todos os item da lista

print('A ordem de apresentação será ')
print(lista)