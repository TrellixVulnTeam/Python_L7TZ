larg = float(input('Digite a largura da parede'))
alt = float(input('Digite a altura da parede'))
area = larg * alt
print ('a parede de dimensão {}x{} tem a area de {} quadrados.'.format(larg,alt,area))
tinta = area / 2
print ('Para pintar a parede, deverá ser utilizado {} litros de tinta'.format(tinta))