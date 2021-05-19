metros = float(input('Digite uma distancia em metro: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A médida de {}m corresponde a:'.format(metros))
print('''{}km
{}hm
{}dam
{}dm
{}cm
{}mm'''.format(km, hm, dam, dm, cm, mm))