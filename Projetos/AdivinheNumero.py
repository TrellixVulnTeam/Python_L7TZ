import random
random=random.randrange(1,20)
chute=0;
while random != chute:
    chute=int(input("Chute um numero de 1 a 20 : "))
    print ("########################")
    chute=int(chute)
    if chute == random:
        print("")
        print("Parabens, o numero e {}.".format(chute))
        break;
    else:
        print("")
        if chute > random:
            print("o numero digitado e maior. Digite um numero menor .")
        else:
            print("o numero digitado e menor. Digite um numero maior .")
print("## FIM DE JOGO")
