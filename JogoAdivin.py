#aprimorando o codigo   (igual ==) (diferente !=) (> < <= >=)
#for in rage(1,10) 1-9
def jogar():
    import random
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    num_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1)Facil (2)Medio (3)Dicícil")

    nivel = int(input("Selecione o nível: "))
    if(nivel == 1):
        total_tentativas = 15
    elif(nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {0} de {1}".format(rodada, total_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Voce digitou", chute_str)
        chute  = int(chute_str)

        if(chute<1 or chute>100):
            print("Voce deve digitar um número entre 1 e 100: ")
            continue
        acetou = chute == num_secreto
        maior  = chute > num_secreto
        menor  = chute < num_secreto

        if (acetou):
            print("voce acertou! PONTUAÇãO: {0}".format(pontos))
            break
        else:
            if(maior):
                print("voce errou! Seu chute foi acima do numero secreto!")
            elif(menor):
                print("voce errou! Seu chute foi menor do numero secreto!")
            pontos_perdidos = abs(num_secreto - chute)
            pontos= pontos - pontos_perdidos
        print("")
    print("FIM DE JOGO!")

if(__name__ == "__main__"):
    jogar()
