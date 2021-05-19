salario = float(input('Qual o salário do funcinário ? R$'))

reajuste = salario + ( salario * (15/100) )

print('Um funcinário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, reajuste))