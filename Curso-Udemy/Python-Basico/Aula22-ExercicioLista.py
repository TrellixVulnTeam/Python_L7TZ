secreto = 'palavra'
letras_digitadas = [] ##construção de uma lista com as letras digitadas
chances = 3

while True:
    if chances <= 0:
        print('Perdeu!!!')
        break
    letra = input('Digite a letra que está na palavra secreta : ')

    if len(letra) > 1 :
        print('Digite apenas uma letra')
        continue

    letras_digitadas.append(letra)
    print('Letra adicionada !!!')

    if letra in secreto:
        print(f'a  letra "{letra}" existe na palavra secreta !!!')
    else:
        print(f'a  letra "{letra}" não existe na palavra secreta !!!')
        letras_digitadas.pop()

    secreto_temporario = '';
    for letra_secreta in secreto:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print("Palavra correta : ")
        break
    else:
        print(f"Dica : A palavra secreta está assim :{secreto_temporario}")

    if letra not in secreto:
        chances -=1

    print(f"Você tem {chances} chances" )
    print()
