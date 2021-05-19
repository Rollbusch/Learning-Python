cotacaoDolar = float(input('Qual a cotação atual do dolar ? U$1 = R$'))
valorEmDolar = float(input('Digite o valor em dolar: U$'))

valorParaReal = cotacaoDolar * valorEmDolar

print('O valor de U${} convertido para real, fica R${}.'.format(valorEmDolar, valorParaReal))