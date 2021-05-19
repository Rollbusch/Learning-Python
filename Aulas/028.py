from random import randint 
from time import sleep 

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente Adivinhar...')
print('-=-' * 20)

escolha = randint(0, 5) # Faz o computador ESCOLHER
num = int(input('Em que número pensei ? '))

print('PROCESSANDO...')
sleep(2) # sleep(segundos) faz o computador ter um tempo de espera baseado nos segundos

if num == escolha:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {}, não no {}.'.format(escolha, num))