n1= input('Digite um numero : ')

if n1.isdigit():
    n1=int(n1)
    print("Numero inteiro")
    if n1 % 2 == 0:
        print(f"{n1} par")
    else:
        print(f"{n1} impar")
else :
    print("Não é um numero inteiro ")