import random

numero_tentativas = 3

numero_secreto = random.randrange(1, 101)
print(numero_secreto)

nivel = int(input(print("[1] Fácil [2] Médio [3] Difícil: ")))
print(nivel)

for rodada in range(1, numero_tentativas + 1):
    print(f" Você tem {numero_tentativas} tentativas para tentar acertar. Tentativa numero {rodada}")
    chute = int(input("Digite um número: "))

    if( chute < 1 or chute > 100):
        print("Você precisa digitar um número entre 1 e 100.")
        continue

    if( chute == numero_secreto):
        print("Parabéns você acertou.")
        break
    else:
        print("Você errou! Tente novamente.")