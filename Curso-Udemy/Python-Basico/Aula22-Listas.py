lista = ['A','B','C','D','E']
print(lista)
print(lista[3])
#lista[3]='GD'
print(lista[3])
print(lista[0:3])
print(lista[:3])
print(lista[2:])
print(lista[-1])
print(lista[::2])
print(lista[::-1])

lk=[1,2,3,4,5,6,7,8]
l1=[1,2,3]
l2=[4,5,6,7,8,9,10,11]
l3=l1 + l2
print(l3)

print(max(lk))
print(min(lk))

l2.append('b')
print(l2)
print(l2[3])

l2.insert(0,'kelsey')
print(l2)
print(l2[0])

l2.pop(-2)
print(l2)

del (l2[4:6])
print (l2)

kcm = list(range(1,10))
soma = 0
for vl in kcm:
    print(vl)
    print(f'O Tipo do {vl} é {type(vl)}')
    soma = soma + vl
print(soma)










