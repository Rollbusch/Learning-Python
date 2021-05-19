vel = int(input('Digite a velocidade: '))

if vel >= 80:
    multa = ( vel - 80 ) * 7
    print('MULTADO! Você excedeu o limite permitido que é de {:.2f}'.format(vel))
    print('Você foi multado em R${}'.format(multa))

else:
    print('Tenha um bom dia! Dirija com segurança.')