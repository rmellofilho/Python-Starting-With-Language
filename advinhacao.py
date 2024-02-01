print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = 42
total_de_tentativas = 3

while (total_de_tentativas > 0):
    print("Tentativa", total_de_tentativas)
    chute = int(input("Digite o seu número: "))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou!", "\nO número secreto é o", chute, end="!")
    elif(maior):
        chute        
        print("Você errou!", "\nO seu chute foi", chute, "e ele é maior que o número secreto!", "\nTente novamente.")
    elif(menor):
        chute
        print("Você errou!", "\nO seu chute foi", chute, "e ele é menor que o número secreto!", "\nTente novamente.")

    total_de_tentativas = total_de_tentativas - 1

    