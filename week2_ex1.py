#jogo da forca
import random

#Definições importantes
tema = input("Escolha um tema dentre: frutas, animais, dificil e paises: ")
palavra = random.choice(tema)
digitadas = []

#Criação do jogo
def jogar():
    global tema
    global palavra
    global digitadas

#Temas da forca
    escolha = {'animais':['lontra', 'jaguatirica', 'baleia', 'canguru', 'elefante', 'gorila', 'macaco', 'doninha'],
            'frutas': ['laranja', 'toranja', 'jabuticaba', 'morango', 'melancia', 'mirtilo', 'framboesa', 'acerola'],
            'paises': ['filipinas', 'paraguai', 'chile', 'brasil', 'marrocos', 'noruega', 'portugal', 'argentina'],
            'dificil': ['rubicundo', 'atarefado', 'afobado', 'transeunte', 'whinderson', 'taciturno', 'araraquara', 'mirabolante']}

#Escolhas do tema (if)
    if tema == 'animais':
        tema1 = escolha["animais"]
        palavra = random.choice(tema1)                     #sorteio da palavra
        tamanho = len(palavra)                             #tamanho da palavra escolhida
        print(f'DICA: A palavra tem {tamanho} letras')     #Quantas letras tem na palavra sorteada
        palavra_secreta = list('_'*tamanho)                #traços de acordo com o tamanho da palavra
        print(palavra_secreta)
                                                    
    elif tema == 'frutas':
        tema2 = escolha["frutas"]
        palavra = random.choice(tema2)
        tamanho = len(palavra)
        print(f'DICA: A palavra tem {tamanho} letras')
        palavra_secreta = list('_'*tamanho)
        print(palavra_secreta)                                

    elif tema == 'dificil':
        tema3 = escolha["dificil"]
        palavra = random.choice(tema3)
        tamanho = len(palavra)
        print(f'DICA: A palavra tem {tamanho} letras')
        palavra_secreta = list('_'*tamanho)
        print(palavra_secreta)        
                            
    elif tema == 'paises':        
        tema4= escolha["paises"]
        palavra = random.choice(tema4)
        tamanho = len(palavra)
        print(f'DICA: A palavra tem {tamanho} letras')
        palavra_secreta = list('_'*tamanho)
        print(palavra_secreta)
                                                        
    else:
        print("Resposta inválida")
        tema = input("Escolha um tema dentre: frutas, animais, paises e aleatorio: ")

#Criação função localizar e alterar letra caso o usuário acerte
    def localizar(texto, palavra):
        posicoes = []
        for i in range(0,len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes

#Criação do loop do jogo   
    while True:
        tentativa = input("Escolha uma letra para adivinhar: ") #começo do jogo
        digitadas.append(tentativa)                             #Adicionar a lista do que já foi tentado

#Para evitar que não chutem uma letra
        if len(tentativa)>1:
            print("ERRO, digite apenas uma letra")
            tentativa = input("Escolha uma letra para adivinhar: ")
        
#Em caso de acerto
        if tentativa in palavra:
            print(f'A letra {tentativa} está contida na palavra')
            print(f'Suas tentativas foram {digitadas}')

#Mudança da palavra_secreta em caso de acerto, uso da função localizar
            posicao = localizar(palavra, tentativa)
            for i in posicao:
                palavra_secreta[i] = tentativa
                print(palavra_secreta)

#Caso o usuario já saiba a palavra                           
            opcao = input("Você já sabe qual é a palavra? sim ou nao? ")
            if opcao == "sim":
                resposta = input("Digite a palavra: ")
                if resposta == palavra:
                    print(f'Parabéns, você acertou! A palavra é {palavra}')
                    break                    
                            
                else:
                    print("Você perdeu!")
                    print(f'A palavra correta era {palavra}')
                    print("GAME OVER")
                    break
                    
            elif opcao == "nao":
                pass
            else:
                print("Resposta inválida. Você já sabe ou não sabe a palavra? Digite sim ou nao")
                opcao = input("Você já sabe qual é a palavra? sim ou nao? ")

#Se errar a letra
        elif not tentativa in palavra:
            print(f'A letra {tentativa} NÃO está contida na palavra')
            print(palavra_secreta)
            print("Essas foram suas tentativas: ", digitadas)

            opcao = input("Você já sabe qual é a palavra? sim ou nao? ")
            if opcao == "sim":
                resposta = input("Digite a palavra: ")
                if resposta == palavra:
                    print(f'Parabéns, você acertou! A palavra é {palavra}')
                    break
                
                else:
                    print("Você perdeu!")
                    print(f'A palavra correta era {palavra}')
                    print("GAME OVER")
                    break
                
            elif opcao == "nao":
                pass
            else:
                print("Resposta inválida. Você já sabe ou não sabe a palavra? Digite sim ou nao")
                opcao = input("Você já sabe qual é a palavra? sim ou nao? ")

jogar()