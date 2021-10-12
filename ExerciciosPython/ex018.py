import math
ang = float(input('Digite o angulo que deseja calcular : '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print ('o seno é : {:.2f} '.format(seno))
print ('o cosseno é : {:.2f} '.format(cos))
print ('a tangente é : {:.2f} '.format(tg))