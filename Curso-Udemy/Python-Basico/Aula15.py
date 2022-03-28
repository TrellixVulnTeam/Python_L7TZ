nome = str(input("Digite seu nome : "))
tm = len(nome)
if tm  <= 4 :
    print("Seu nome é curto ")
if tm > 4 and tm <= 6 :
    print("Seu nome é normal ")
elif tm > 6 :
    print("Seu nome é grande ")
print("seu nome tem : ",len(nome))
