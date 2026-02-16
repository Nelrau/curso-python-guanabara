resposta = f'resultado de uma classe, é a instanciação de uma classe, é o que tem estado e comportamento. Elemento material ou abstrato que e descrito por meio de atributos, métodos e estado atual.'
print('O que é um objeto?\n', resposta)

resposta = f'''Formato a ser seguido, para padronizar a criação de objetos.nome da classe, 
caracteristica da classe ou atributos, 
metodos ou coisas que posso fazer, onde tem parenteses.'''
print('O que é uma classe?\n', resposta)

resposta = f'Quando um objeto é criado com base em uma classe.'
print('Quando acontece um instanciamento?\n', resposta)

resposta = f'O estado de um objeto é definido pelos valores dos seus atributos em um determinado momento.'
print('Sabe definir o estado de um objeto?\n', resposta)

print("""011 - Qual dos objetos abaixo seria o unico abstrato da lista?
      A) Sensor
      B) Robô
      C) Notificacao
      D) Livro
      """)
resposta = input("desafio 011 - Resposta: ")
p = 0
if resposta.upper() == "C":
    print("Resposta correta!")
    p += 1
else:    
    print("Resposta incorreta. A resposta correta é C) Notificacao.")

print("""012 - Na a teoria de OO, o termo usado para o ato de fazer um objeto existir, a partir de uma classe se chama:
      A) Instanciar
      B) classificar
      C) objetificar
      D) forjar
        """)
resposta = input("desafio 012 - Resposta: ")
if resposta.upper() == "A":
    print("Resposta correta!")
    p += 1
else:    
    print("Resposta incorreta. A resposta correta é A) Instanciar.")

print("""013 - Todo objeto tem uma lista de atividades que podem ser realizado com ele ou que ele pode realizar sozinho,que são:
        A) Atributos
        B) Metodos
        C) classes
        D) instancias
        """)
resposta = input("desafio 013 - Resposta: ")
if resposta.upper() == "B":
    print("Resposta correta!")
    p += 1
else:    
    print("Resposta incorreta. A resposta correta é B) Metodos.")

print("""014 - Ao conjunto de todos os valores de atributos de um objeto im um determinado momento, damos o nome de:
        A) Identidade
        B) Instância
        C) Método
        D) Estado
        """)
resposta = input("desafio 014 - Resposta: ")
if resposta.upper() == "D":
    print("Resposta correta!")
    p += 1
else:    
    print("Resposta incorreta. A resposta correta é D) Estado.")
    
print("""015 - Coloque nos comentários a estrutura de dois objetos: um concreto e um abstrato.
Inclua também seus principais atributos, métodos e crie um exemplo de estado para cada um deles.""")

resposta = input("desafio 015 - Resposta: ")
