from jogos import forca
from jogos import advinhacao

print("===============================")
print("******Escolha o seu jogo!******")
print("===============================")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    forca.jogar_forca()
elif(jogo == 2):
    advinhacao.jogar_advinhacao()