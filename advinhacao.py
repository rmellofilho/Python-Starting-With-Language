print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = 42

chute = int(input("Digite o seu número: "))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("Você acertou!", "\nO número secreto é o", chute, end="!")
elif(maior):
    print("Você errou!", "\nO seu chute foi", chute, "e ele é maior que o número secreto!")
elif(menor):
    print("Você errou!", "\nO seu chute foi", chute, "e ele é menor que o número secreto!")