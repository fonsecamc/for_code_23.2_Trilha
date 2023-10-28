import os      #para utilizar o cls
import math    #para utilizar o logaritmo de base e

n = 2          #nº inicial do somatório
somatorio = 0

while n < 100000:
  os.system('cls')
  somatorio += 1/(n*(math.log(n,math.e))**2) 
  n = n + 1
  print(somatorio)