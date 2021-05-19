vendedor = input('Nome do vendedor: ')
numeroPeca = input('Número da peça: ')
precoUnit = float(input('Preço unitário: '))
qntdVendida = int(input('Quanditade vendida: '))

totalVendido = precoUnit * qntdVendida
comissao = totalVendido + ( totalVendido * (5/100) )

print('----------')
print('''Vendedor: {}
Código da peça: {}
Preço unitário: {}
Quantidade vendida: {}
Comissão a receber: {:.2f}'''.format(vendedor, numeroPeca, precoUnit, qntdVendida, comissao))
print('----------')