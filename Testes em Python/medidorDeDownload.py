net = int(input('Quantos MB de net você tem ? ')) / 8 

tamanhoArquivo = float(input('Digite o tamanho do arquivo em GB: ')) * 1024

demora = ( tamanhoArquivo / net ) / 60
demora2 = demora / 60

print('O download irá demorar {:.2f} hora(s).'.format(demora2))
