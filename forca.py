import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    enforcou = False
    acertou = False
    erros = 6


    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_faltando = str(letras_acertadas.count("_"))
    print(letras_acertadas)
    print("Ainda faltam acertar {} letras".format(letras_faltando))

    while (not enforcou and not acertou):

        print("Você ainda tem {} tentativas.".format(erros))
        
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
                index = 0
                for letra in palavra_secreta:
                        if (chute == letra):
                                letras_acertadas[index] = letra
                        index = index + 1
        else:
                erros -= 1

        print(letras_acertadas)
        letras_faltando = letras_acertadas.count("_")
        print("Ainda falta acertar {} letras".format(letras_faltando))

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas

    if (acertou):
                print("Você ganhou!!!!")
    else:
                print("Você perdeu!!!!")

def imprime_mensagem_abertura():
    print("---------------------------")
    print("-----------Forca-----------")
    print("---------------------------")

def carrega_palavra_secreta():
    palavras = []
    with open("arquivo.txt") as arquivo:
        for fruta in arquivo:
                fruta = fruta.strip()
                palavras.append(fruta)
        arquivo.close()

    numero = random.randrange(0,len(palavras))
    return palavras[numero].upper()


if (__name__ == "__main__"):
    jogar()