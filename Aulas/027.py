nome = str(input('Digite seu nome completo: ')).strip().title()
print('Muito prazer em te conhecer!')
separar = nome.split()
print('Seu primeiro nome é {}'.format(separar[0]))
print('Seu último nome é {}'.format(separar[-1]))