print ("Calculo salarial : ")
sal_atual = int(input("Digite o salario : "))
if sal_atual <= 280:
    print ("salario atual : ", sal_atual)
    print ("o percentual aplicado sera de 20 %")
    valor_aumento = (20 * sal_atual)/100
    print ("valor aumento :  ", valor_aumento)
    novo_sal = sal_atual + valor_aumento
    print(" valor do novo salario :", novo_sal)
if sal_atual > 280 and sal_atual <=700:
    print ("salario atual : ", sal_atual)
    print ("o percentual aplicado sera de 15 %")
    valor_aumento = (15 * sal_atual)/100
    print ("valor aumento :  ", valor_aumento)
    novo_sal = sal_atual + valor_aumento
    print(" valor do novo salario :", novo_sal)
if sal_atual > 700 and sal_atual <=1500:
    print ("salario atual : ", sal_atual)
    print ("o percentual aplicado sera de 10 %")
    valor_aumento = (10 * sal_atual)/100
    print ("valor aumento :  ", valor_aumento)
    novo_sal = sal_atual + valor_aumento
    print(" valor do novo salario :", novo_sal)
if sal_atual > 1500:
    print("salario atual : ", sal_atual)
    print("o percentual aplicado sera de 5 %")
    valor_aumento = (5 * sal_atual) / 100
    print("valor aumento :  ", valor_aumento)
    novo_sal = sal_atual + valor_aumento
    print("valor do novo salario :", novo_sal)