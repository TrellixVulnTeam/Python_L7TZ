import dns.resolver
dominio = str(input('Digite o Dominio : '));
Tipo_registro = str(input("Digite o tipo de registro : "));
if Tipo_registro:
    result = dns.resolver.resolve(dominio,Tipo_registro)
    for r in result:
        print(r.to_text())
else:
    print("Preencha o tipo de resistro")
