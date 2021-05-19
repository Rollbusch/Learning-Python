nome = str(input('Digiter seu nome completo: ')).strip() # .strip() elimina os espaços antes e depois da STR.

print('Analisando seu nome...')

print(nome)

print('Seu nome em maíusculas é: {}.'.format(nome.upper()))
print('Seu nome em minúsculas é: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))# .count() conta os caracteres especificos dentro do ().
# print('Seu primeiro nome tem {}.'.format(nome.find(' ')))    # .find() procura um caracter especifico e conta em que posição ele está.
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0]))) 