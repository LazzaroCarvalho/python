from math import sin, cos, tan, radians
ang=float(input('Digite o angulo desejado para calculo do SEN, COS, TAN: '))
seno= sin(radians(ang))
cose= cos(radians(ang))
tang= tan(radians(ang))
print('O Valor do Seno de {}  é {}'.format(ang, seno))
print('O Valor do Cosseno de {}  é {}'.format(ang, cose))
print('O Valor do Tangente de {} é {}'.format(ang, tang))

