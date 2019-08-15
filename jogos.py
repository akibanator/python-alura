import forca
import adivinhacao

def escolher_jogo():
    imprime_mensagem_abertura()

    jogo = int(input("Qual jogo: "))

    if (jogo == 1):
        print("Iniciando jogo da Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Iniciando jogo da Adivinhacao")
        adivinhacao.jogar()

def imprime_mensagem_abertura():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

if (__name__ == "__main__"):
    escolher_jogo()