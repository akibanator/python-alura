import random

def jogar():
    print("---------------------------")
    print("--------Adivinhacao--------")
    print("---------------------------")

    adivinhar_numero = random.randrange(1,101)
    validacao_de_entrada = True
    pontos = 1000
    pontos_perdidos = 0

    while(validacao_de_entrada):
        total_tentativas = input("Digite o número de tentativas(1-15) que o jogador terá para acertar o número: ")
        total_tentativas_int = int(total_tentativas)
        if (total_tentativas_int >= 1 and total_tentativas_int <= 15):
            break
        else:
            print("Valor inválido")
        
    tentativa = 1

    while(total_tentativas_int>=tentativa):

        print("Tentativa {} de {}".format(tentativa,total_tentativas))

        numero_chutado = input("Digite um numero de 1 - 100: ")

        numero_chutado_int = int(numero_chutado)

        if (numero_chutado_int < 1 or numero_chutado_int > 100):
            print("Você digitou um número inválido, digite um número de 1 - 100")
            continue

        #print(type(numero_chutado))
        #print(type(numero_chutado_int))

        maior = adivinhar_numero < numero_chutado_int
        menor = adivinhar_numero > numero_chutado_int
        certo = adivinhar_numero == numero_chutado_int

        if (certo):
            print("Você acertou!")
            print("Sua pontuação é: {}".format(pontos))
            break
        else:
            pontos_perdidos = numero_chutado_int - adivinhar_numero
            pontos = pontos - abs(pontos_perdidos)
            if (maior):
                print("Tente um número menor")
            elif (menor):
                print("Tente um número maior")
        
        if (tentativa==total_tentativas_int):
            print("Você não conseguiu acertar! Sua pontuação é: {}".format(pontos))

        tentativa = tentativa + 1

if (__name__ == "__main__"):
    jogar()