from datetime import date
ano = int(input('Que ano quer analisar ? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year # importa o ano do dia de hoje.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano É bissexto')
else:
    print('O ano NÃO É bissexto')
print('Ano analisado: {}'.format(ano))