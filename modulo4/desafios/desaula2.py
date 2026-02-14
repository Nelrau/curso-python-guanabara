p = 0
print("aula 2 - 6 vantagens do poo - Curso de Python 3")
print("""
      C - confiavel: o isolamento das partes do sistema torna o código mais confiável, pois os erros em uma parte não afetam as outras partes.
      O - oportuno: Ao dividir em partes, cada uma parte pode ser desenvolvida e testada de forma independente, o que torna o desenvolvimento mais rápido e eficiente.
      M - manutenivel: Atualizar é mais fácil. Uma pequena mudança vai beneficiar o sistema inteiro, sem a necessidade de alterar o código em outros lugares.
      E - executavel: Um sistema não deve ser estatico. Tudo deve mudar e crescer para permanecer util.
      R - reutilizavel: Objetos que foram criados para um projeto podem ser reutilizados em outros projetos, economizando tempo e esforço.
      N - natural: Mais facil de entender. Maior atenção as funcionalidades do que a detalhes de implementação. 
      """)
print("""006 - Criei um sistema para Escola. Ao criar outro sistema para Academia, parte do trabalho ja estará feito, pois tenho Alunos nos dois?
A) Confiavel
B) Natural
C) Manutenivel
D) Reutilizavel
""")
resposta = input("desafio 006 - Resposta: ")

if resposta.upper() == "D":
    print("Resposta correta!")
    p += 1
else:
    print("Resposta incorreta. A resposta correta é D) Reutilizavel.")
    
print("""007 - Se pecisar adicionar uma nova funcionalidade ao sistema, consigo fazer isso com grande facilidade
      A) Natural
      B) Extensivel
      C) Reutilizavel
      D) Oportuno
      """)
resposta = input("desafio 007 - Resposta: ")
if resposta.upper() == "B":
    print("Resposta correta!")
    p += 1
else:
    print("Resposta incorreta. A resposta correta é B) Extensivel.")
    
print("""008 - Posso desenvolver varias funções que dependem de outras ao mesmo tempo, se o planejamento for seguido?

      A) Oportuno
      B) Reutilizavel
      C) Confiavel
      D) Manutenivel
      """)
resposta = input("desafio 008 - Resposta: ")
if resposta.upper() == "D":
    print("Resposta correta!")
    p += 1
else:
    print("Resposta incorreta. A resposta correta é D) Manutenivel.")
    
print("""009 - O codigo fica muito simples de ler e de compreender, ja que não preciso me preocupar com detalhes de funcionamento ao programar.
        A) Natural
        B) Extensivel
        C) Manutenivel
        D) Oportuno
        """)
resposta = input("desafio 009 - Resposta: ")
if resposta.upper() == "A":
    print("Resposta correta!")
    p += 1
else:    print("Resposta incorreta. A resposta correta é A) Natural.")

print("""010 - Posso alterar como uma funcionalidade trabalha e tudo continua funcionando como antes.
        A) Oportuno
        B) Reutilizavel
        C) Confiavel
        D) Natural
        """)
resposta = input("desafio 010 - Resposta: ")
if resposta.upper() == "C":
    print("Resposta correta!")
    p += 1
else:
    print("Resposta incorreta. A resposta correta é C) Confiavel.")
print(f"Voce acertou {p} de 5 perguntas.")