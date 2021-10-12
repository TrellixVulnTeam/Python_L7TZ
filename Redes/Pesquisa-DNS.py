###A, MX, NS, AAAA, SOA, TXT
import dns
import dns.resolver
import dns.name
import sys
import os



##### Faz queries nos DNS #####
regA = dns.resolver.query(sys.argv[1],'A')
for reg in regA:
    print ('Ip domínio: '+ str(reg))


regMX = dns.resolver.query(sys.argv[1],'MX')
for reg in regMX:
    print ('Servidores E-mail : ' + str(reg))


regNS = dns.resolver.query(sys.argv[1],'NS')
for reg in regNS:
    print ('Servidores DNS:' + str(reg))


regSOA = dns.resolver.query(sys.argv[1],'SOA')
for reg in regSOA:
    print ('Informacoes : DnsPrincipal responsavel Serial tempooRefresh retry expiracao tempoMinimo : ' +str(reg))

regTXT = dns.resolver.query(sys.argv[1],'TXT')
for reg in regTXT:
    print ('registros SPF :' +str(reg))

regAAAA = dns.resolver.query(sys.argv[1],'AAAA')
for reg in regAAAA:
    print ('Endereco IPv6 :' +str(reg))