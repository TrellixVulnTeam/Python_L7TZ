import dns.name
reg1 = dns.name.from_text('portal.cooxupe.com.br')
reg2 = dns.name.from_text('cooxupe.com.br')
result = (reg1.is_subdomain(reg2))
print (result)