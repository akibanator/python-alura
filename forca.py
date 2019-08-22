import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    mostra_qtd_letras(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 7

    while (not enforcou and not acertou):

        print("Você ainda tem {} tentativas.".format(erros))
        
        chute = pede_chute()

        if chute in palavra_secreta:
                marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
                erros -= 1
                desenha_forca(erros)

        print(letras_acertadas)
        letras_faltando = letras_acertadas.count("_")
        print("Ainda falta acertar {} letras".format(letras_faltando))

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas

    if (acertou):
                imprime_mensagem_ganhador()
    else:
                imprime_mensagem_perdedor(palavra_secreta)

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
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()