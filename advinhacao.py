print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = 42

chute = int(input("Digite o seu número: "))

if (chute == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")