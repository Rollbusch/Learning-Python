real = float(input('Quanto dinheiro você tem na carteira ? R$'))

dolar = real / 3.27

print('Com R${} você pode comprar U${:.2f}'.format(real, dolar))