km = float(input('Qual a distancia da viagem em KM ? '))

preco = km * 0.50 if km <= 200 else km * 0.45 # Um metodo diferente de usar condições.
print('O preço da passagem será de R${:.2f}'.format(preco))

'''preco = 0

if km <= 200:
    preco = km * 0.5
    print('A viagem de {} custará R${:.2f}'.format(km, preco))
else:
    preco = km * 0.45
    print('A viagem de {} custará R${:.2f}'.format(km, preco))'''
