letra = str(input('Digite uma letra : ')).lower()
if letra =='a' or letra =='e' or letra =='i' or letra=='o' or letra =='u':
    print ('a letra {} é uma vogal'.format(letra))
else:
    print ('a letra {} é uma consoante '.format(letra))