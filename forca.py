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
        
        chute = pede_chute()

        if chute in palavra_secreta:
                marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
                erros -= 1

        print(letras_acertadas)
        letras_faltando = letras_acertadas.count("_")
        print("Ainda falta acertar {} letras".format(letras_faltando))

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas

    if (acertou):
                imprime_mensagem_ganhador()
    else:
                imprime_mensagem_perdedor()

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

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
        index = 0
        for letra in palavra_secreta:
                if (chute == letra):
                        letras_acertadas[index] = letra
                index = index + 1

def imprime_mensagem_ganhador():
        print("Você ganhou!!!!")

def imprime_mensagem_perdedor():
        print("Você perdeu!!!!")

if (__name__ == "__main__"):
    jogar()