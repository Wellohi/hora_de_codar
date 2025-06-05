import random 

num_secreto = random.randint(1, 100)

tentativas = 0

hist_pontuacao = []

print("Jogo de adivinhação de número")

while True:
    num_adivinhado = input("Digite um número: ")
    
    if not num_adivinhado.isdigit():
        print('Digite um número valido: 1 à 100')
        continue
    
    num_adivinhado = int(num_adivinhado)
    tentativas += 1
    pontuacao = round((100/tentativas),2)
    hist_pontuacao.append(pontuacao)

    if num_adivinhado == num_secreto:
        print("Acertou, o número era: ", num_secreto)
        print(f"Pontuação: {hist_pontuacao}, Tentativas: {tentativas}")
        break
    
    elif num_adivinhado != num_secreto:
        if num_adivinhado > num_secreto:
            print("Errado, o número é menor")
            
        elif num_adivinhado < num_secreto:
            print("Errado, o número é maior")
            
    else:
        print("Invalido, tente novamente")

            
        