print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = 42

chute = int(input("Digite o seu número: "))

if (chute == numero_secreto):
    print("Você acertou!", "\nO número secreto é,", chute)
else:
    print("Você errou!", "\nO número que você digitou foi o", chute)