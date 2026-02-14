p = 0
print("""001 - Em que década aconteceu a 'Crise do sofware', no mercado ?
      A) 1950
      B) 1960
      C) 1980
      D) 2000 """)

resposta = input("Digite a década ou a letra correspondente: ")
if resposta == "1960" or resposta == "B":
    print("Parabéns! Você acertou.")
    p += 1
else:
    if resposta == "1980" or resposta == "1950" or resposta == "2000":
        print("Resposta incorreta. A década correta é 1960.")
    else:
        print("Resposta inválida. A década correta é 1960.")
        
        
        
print("""002 - Qual das características a seguir identifica as primeiras linguagens lineares ?
      A) Maior modularidade
      B) Desvios forçados em GOTO
      C) Estrutura de controle
      D) Intruções de baixo nível """)

resposta = input("Digite a letra correspondente: ")
if resposta == "B" or resposta == "Desvios forçados em GOTO":
    print("Parabéns! Você acertou.")
    p += 1
else:
    if resposta == "A" or resposta == "C" or resposta == "D":
        print("Resposta incorreta. A característica correta é 'Desvios forçados em GOTO'.")
    else:
        print("Resposta inválida. A característica correta é 'Desvios forçados em GOTO'.")


print("""003 - Quem foi o criador da linguagem 'Smalltalk', uma das primeiras linguagens orientadas a objetos ?
      A) Edsger Dijkstra
      B) Guido van Rossum
      C) Alan Kay
      D) Kristen Nygaard """)

if resposta == "C" or resposta == "Alan Kay":
    print("Parabéns! Você acertou.")
    p += 1
else:
    if resposta == "A" or resposta == "B" or resposta == "D":
        print("Resposta incorreta. O criador correto é 'Alan Kay'.")
    else:
        print("Resposta inválida. O criador correto é 'Alan Kay'.")



print("""004 - A linguagem 'Simula' foi  um superconjunto de que outra linguagem de programação ?
      A) Algol
      B) C
      C) Smalltalk
      D) Python """)
resposta = input("Digite a letra correspondente: ")
if resposta == "A" or resposta == "Algol":
    print("Parabéns! Você acertou.")
    p += 1
else:    
    if resposta == "B" or resposta == "C" or resposta == "D":
        print(f"{resposta} Resposta incorreta. A linguagem correta é 'Algol'.")

    else:
        print("Resposta inválida. A linguagem correta é 'Algol'.")
        
        
        
        
print("""005 - Na sigla 'OOAD' as ultimas duas letras significam
      A) Algol / Dashboard
      B) Algorithms / Digital
      C) Analytics / Default
      D) Analysis / Design""")
resposta = input("Digite a letra correspondente: ")
if resposta == "D" or resposta == "Analysis / Design":
    print("Parabéns! Você acertou.")
    p += 1
else:
    if resposta == "A" or resposta == "B" or resposta == "C":
        print("Resposta incorreta. As palavras corretas são 'Analysis / Design'.")
    else:
        print("Resposta inválida. As palavras corretas são 'Analysis / Design'.")
