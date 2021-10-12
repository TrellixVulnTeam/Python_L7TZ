import dns.resolver
dominio: str = input("Alvo : ")
registros = ["AAAA","AA" ,"NS" ,"TXT" ,"MX"]
for registro in registros:
    resultado = dns.resolver.query(dominio, registro, raise_on_no_answer=True)
    if resultado.rrset is not None:
        print(resultado.rrset)