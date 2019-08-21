import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    mostra_qtd_letras(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 6

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

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def mostra_qtd_letras(letras_acertadas):
    letras_faltando = str(letras_acertadas.count("_"))
    print(letras_acertadas)
    print("Ainda faltam acertar {} letras".format(letras_faltando))

if (__name__ == "__main__"):
    jogar()