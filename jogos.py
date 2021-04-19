import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("******* Escolha Seu Jogo ********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo:  "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    else:
        print("Jogando Advinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__== "__main__"):
    escolhe_jogo()
