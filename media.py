n1 = float(input('Digite sua primeira Nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('digite sua terceira nota: '))

media = ((n1 + n2 + n3)/3)

print('A sua média é {}'.format(media))

if media >= 6.0:
 print('Parabens')

else:
 print('Estude mais')
