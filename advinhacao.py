import random

print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0
nivel = int(input("Defina o nível de 1 a 3: "))
pontos = 100
print(numero_secreto)

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = int(input("Digite um número entre 1 e 100: "))



    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!", "\nVocê fechou com {0} pontos e o número secreto foi o {1}!".format(pontos, chute))
        break
    else:
        if(maior):  
            print("Você errou!", "\nO seu chute foi", chute, "e ele é maior que o número secreto!", "\nTente novamente.")
        elif(menor):
            print("Você errou!", "\nO seu chute foi", chute, "e ele é menor que o número secreto!", "\nTente novamente.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
print("\n")

print("Fim de jogo!")
    