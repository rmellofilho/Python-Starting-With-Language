from jogos import forca
from jogos import advinhacao

print("===============================")
print("******Escolha o seu jogo!******")
print("===============================")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo? "))


def escolhe_jogo():
    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        advinhacao.jogar()


if(__name__ == "__main__"):
    escolhe_jogo()