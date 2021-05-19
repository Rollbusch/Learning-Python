tempoGasto = int(input('Digite o tempo gasto em horas: '))
velocidadeMedia = int(input('Digite a velocidade média: '))

gastoNaViagem = ( tempoGasto * velocidadeMedia ) / 12


print('O seu carro gasta {}Lts na viagem.'.format(gastoNaViagem))