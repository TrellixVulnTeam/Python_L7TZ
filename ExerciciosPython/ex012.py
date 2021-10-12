pr = float(input('Digite o valor do produto'))
ds = float(input('Digite o valor do desconto'))
vp   = pr - (pr*ds/100)
print ('o produto que custava {} com desconto de {} custara {} '.format(pr,ds,vp))