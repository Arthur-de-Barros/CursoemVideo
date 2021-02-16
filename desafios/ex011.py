altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede: '))
area = altura*largura
tinta = area/2
print('A area da parede é {}A, e vai precisar de: {:.1f}L, para pintar ela por completo'.format(area, tinta))
