from datetime import date

nasci = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasci

print('Quem nasceu em {} tem {} anos em {}'.format(nasci, idade, atual))

if idade == 18:
    print('Você precisa de alistar IMEDIATAMENTE')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você devia ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))