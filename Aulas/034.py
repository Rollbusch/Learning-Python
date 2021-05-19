salario = float(input('Digite o salário: R$'))
total = 0
if salario <= 1250:
    total = salario + ( salario * (15/100))
    print('Quem ganhava R${}, passa a ganhar R${:.2f} agora.'.format(salario, total))
else:
    total = salario + ( salario * (10/100))
    print('Quem ganhava R${}, passa a ganhar R${:.2f} agora.'.format(salario, total)) 