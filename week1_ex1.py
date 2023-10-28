import random
#Melhor de três
rodada = 1

#Pedra, papel ou tesoura? (imposição do nº de tentativas)
pergunta = input(f'Rodada {rodada} de 5. Escolha pedra, papel ou tesoura: ')

#Escolhas possível para o computador
escolhas = ("pedra", "papel", "tesoura")
escolha_computador = random.choice(escolhas)
print("escolha do computador: ",escolha_computador)
pontos = 0

#Rodagem do código no nº de tentativas estipulado e montagem do que é vencer, empatar ou perder
while rodada <= 5:  
  if pontos <= 3 and pontos >= -3:
    if escolha_computador == "pedra":
      if pergunta == "pedra":           
        print('\nEmpate') 
      elif pergunta == "papel":
        print('\nVocê ganhou')
        pontos = pontos + 1    
      elif pergunta == "tesoura":
        pontos = pontos - 1
        print('\nVocê perdeu')    
      else:
        print("\nResposta Inválida. Escolha pedra, papel ou tesoura")
        break

    elif escolha_computador == "papel":
      if pergunta == "pedra":
        pontos = pontos - 1
        print('\nVocê perdeu')   
      elif pergunta == "papel":  
        print('\nEmpate') 
      elif pergunta == "tesoura":
        print('\nVocê ganhou')
        pontos = pontos + 1       
      else:
        print("\nResposta Inválida. Escolha pedra, papel ou tesoura")
        break

    elif escolha_computador == "tesoura":
      if pergunta == "pedra":        
        print('\nVocê ganhou')
        pontos = pontos + 1           
      elif pergunta == "papel":        
        print('\nVocê perdeu.')   
        pontos = pontos - 1  
      elif pergunta == "tesoura":            
        print('\nEmpate.') 
      else:
        print("\nResposta Inválida. Escolha pedra, papel ou tesoura")

  if rodada == 5:
    print("\nNúmero de tentativas acabaram :/")
    if pontos >= 2:
      print("\nVocê ganhou o jogo!")
    elif pontos < 2:
      print("\nVocê perdeu o jogo!")
    else:
      print("\nDeu empate") 
    break

  rodada = rodada + 1
  pergunta = input(f'\nRodada {rodada} de 5. Escolha pedra, papel ou tesoura: ')
  escolhas = ("pedra", "papel", "tesoura")
  escolha_computador = random.choice(escolhas)
  print("escolha do computador: ",escolha_computador)