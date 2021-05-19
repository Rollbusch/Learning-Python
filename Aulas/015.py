kmRodado = int(input('Digite quantos KM foi rodado: '))
diasAlugado = int(input('Digite quantos dias foram alugados: '))

diaPreco = diasAlugado * 60
kmPreco = kmRodado * 0.15
total = diaPreco + kmPreco

print('O total a pagar é de R${}'.format(total))