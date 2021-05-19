algo = str(input('Digite algo: '))

print(type(algo))

print('Só tem espaços ? ', algo.isspace()) # .isspace() verifica se só há espaços.
print('É um numérico ? ', algo.isnumeric()) # .isnumeric() verifica se é um número ( mesmo sendo <str> ).
print('É alfabético ? ', algo.isalpha()) # .isalpha() verifica se é somente alfabético.
print('É alfanumérico ? ', algo.isalnum()) # .isalnum() verifica se é alfanumérico ( alfabético + numéro ).
print('Está em maiúsculas ? ', algo.isupper()) # .isupper() verifica se está tudo em maiúsculas.
print('Está em minúsculas ? ', algo.islower()) # .islower() verifica se está tudo em minúsculas.
print('Está capitalizada ? ', algo.istitle()) # .istitle() verifica se está capitalizada ( primeira letra maiúscula )