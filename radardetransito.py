from random import choice
lista = [30,40,50,60,70,75,80,81,82,83,90,100,111,150,220,180]
vel = choice(lista)
velmax = int(80)
if vel > velmax:
    velexc = int(vel - 80)
    multa = int(velexc * 7)
    print('Você excedeu a velociade maxima da via {}Km/h, passando a "{}Km/h", e sera multado no valor R${:.2f}'.format(velmax, vel, multa))
else:
    print('De acordo com a velocidade permitida pela via {}Km/h'.format(vel))
