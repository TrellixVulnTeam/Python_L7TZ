turno = str(input('Em que voce estuda : M:MATUTINO V:VESPERTINO N:NOTURNO : ')).upper()
if turno =='M':
    print('Turno Matutino')
if turno =='V':
    print('Turno Vespertino')
if turno =='N':
    print('Turno Noturno')
if turno != 'M' and turno != 'V' and turno !='N':
    print ('Invalido')