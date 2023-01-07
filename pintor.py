import select

alt = float(input('Digite a altura da sua parede: '))
lar = float(input('Digite a largura da sua parede: '))
litro = 2 * 2

qtd = (alt * lar)/litro
m = alt * lar
print('A parede possui {}M²'.format(m))
print('A quantidade de tinta necessária para a pintura dessa parede é de {} Litros'.format(qtd))

