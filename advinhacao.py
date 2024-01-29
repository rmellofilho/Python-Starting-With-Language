print("===============================")
print("Bem vindo ao Jogo de Advinhação")
print("===============================")


numero_secreto = 42

chute = int(input("Digite o seu número: "))

if (chute == numero_secreto):
    print("Você acertou!", "\nO número secreto é o", chute, end="!")
elif(chute > numero_secreto):
    print("Você errou!", "\nO número que você digitou foi o", chute, ", ele é maior que o número secreto!")
elif(chute < numero_secreto):
    print("Você errou!", "\nO número que você digitou foi o", chute, ", ele é menor que o número secreto!")
else:
    print("Você errou!", "\nO número que você digitou foi o", chute)