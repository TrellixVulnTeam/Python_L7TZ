#do maior para o menor
n1 = input("Numero um : ")
n2 = input("numero dois : ")
n3 = input("nunero tres  :")
mt=[]
maior=n1
if n3 > n2:
    aux = n3;
    n3 = n2;
    n2 = aux;
if n2 > n1:
    aux = n2;
    n2 = n1;
    n1 = aux;
if n3 > n2:
    aux = n3;
    n3 = n2;
    n2 = aux;
print ("ordem decrescente : ", n1, n2, n3)