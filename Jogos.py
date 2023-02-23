import forca
import JogoAdivin
def escolhe_jogo():
    print("********************************")
    print("********Escolha seu jogo********")
    print("********************************")

    print("(1)Forca (2)Advinhação")

    jogo = int(input("Qual jogo: "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        JogoAdivin.jogar()
if(__name__ == "__main__"):
    escolhe_jogo()