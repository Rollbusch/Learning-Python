nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = ( nota1 + nota2 ) / 2

print('Você tirou na primeira prova {}, e na segunda {}. Sua média é de {}.'.format(nota1, nota2, media))

if media >= 7:
    print('Você está APROVADO!')
elif 7 > media >= 5: # 7 maior que media que é maior igual a 5
    print('Você está de recuperação.')
elif media < 5:
    print('Você está REPROVADO.')