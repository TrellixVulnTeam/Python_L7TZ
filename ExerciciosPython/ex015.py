dias = float(input('Digite a quantidade de dias alugados'))
km = float(input('Digite a quantidade de KM percorridos'))
vdia = 60*dias
vkm = 0.15*km
v_total = vdia + vkm
print ('a quantidade de dias foi de {}, rodando {} KM,sendo pagar é de RS{:.2f}: '.format(dias,km, v_total))