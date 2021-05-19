valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário: R$'))
anos = int(input('Digite quantos anos você deseja pagar: '))

trintaSalario = salario * (30/100)
prestacao = valorCasa / ( anos * 12 )

print('Para pagar uma casa de R${:.2f} em {} anos, será necessário R${:.2f} mensais.'.format(valorCasa, anos, prestacao))

if prestacao <= trintaSalario:
    print('EMPRÉSTIMO APROVADO')
else:
    print('EMPRÉSTIMO RECUSADO')