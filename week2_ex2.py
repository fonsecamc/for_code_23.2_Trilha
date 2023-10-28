import random
escolhas = ["pedra", "papel", "tesoura"]

#Jogadores
pontos_do_computador = 0
pontos_do_usuario = 0

#Definindo derrota
def perdeu():
    global pontos_do_computador
    pontos_do_computador += 1
    print("Você perdeu essa rodada")
    print("\nPlacar: (PC x Usuário) ", pontos_do_computador, " X ", pontos_do_usuario)

#Definindo vitória
def ganhou():
    global pontos_do_usuario
    pontos_do_usuario += 1
    print("Você ganhou essa rodada")
    print("\nPlacar: (PC x Usuário) ", pontos_do_computador, " X ", pontos_do_usuario)

#inicialização do jogo
while True:
    usuario = input("pedra, papel ou tesoura? ")
    computador = random.choice(escolhas)

#Definição de empate
    if usuario == computador:
        print("O computador escolheu: ", computador)
        print("\nDeu empate, ninguém pontuou")

#Possibilidade de dar Vitória
    elif usuario == "pedra" and computador == "tesoura" or usuario == "papel" and computador == "pedra" or usuario == "tesoura" and computador == "papel":
        print("O computador escolheu: ", computador)
        ganhou()

#Possibilidade de dar Derrota
    elif usuario == "pedra" and computador == "papel" or usuario == "papel" and computador == "tesoura" or usuario == "tesoura" and computador == "pedra":
        print("O computador escolheu: ", computador)
        perdeu()

#Definindo o que o usuário pode escrever
    else:
        print("Resposta inválida")
        input("pedra, papel ou tesoura? ")

#Quem fizer 3 pontos primeiro ganha
    if pontos_do_usuario >= 3:
        print("\nVocê ganhou o jogo!")
        break
    elif pontos_do_computador >= 3:
        print("\nVocê perdeu o jogo!")
        break
    elif pontos_do_usuario == 3 and pontos_do_computador == 3:
        print("Deu empate")
        break