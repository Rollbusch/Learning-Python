num = int(input('Digite um número: '))

x2 = num * 2 
x3 = num * 3
raiz = num**(1/2)
raiz2 = pow(num, (1/2)) # pow() = potencia, base = 1° casa, expoente = 2° casa

print('O dobro de {} é: {}.'.format(num, x2))
print('O triplo de {} é: {}.'.format(num, x3))
print('A raiz quadrada de {} é: {:.2f}.'.format(num, raiz))
print('A raiz quadrada de {} é: {:.2f}.'.format(num, raiz2))