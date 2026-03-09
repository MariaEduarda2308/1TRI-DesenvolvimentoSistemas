# importação da biblioteca
import random

# menu de opções usando o terminal
while True:
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    opcao = int(input("Digite a opção desejada (1 a 3)"))

    if opcao == 1:
        print("Selecionado opção 1")
        sorteio_max = 10
        tentativas_max = 3
    elif opcao == 2:
        print("Selecionado opção 2")
        sorteio_max = 50
        tentativas_max = 6
    elif opcao == 3:
        print("Selecionado opção 3")
        sorteio_max = 100
        tentativas_max = 10
    else:
        print("Opção inválida, selecionado Opção Difícil")
        sorteio_max = 100
        tentativas_max = 10

    # Configurações do jogo
    tentativas = 1
    errou = True
    numero = random.randint(0,sorteio_max)


    while (tentativas <= tentativas_max):
        print("Tentativa:", tentativas)
        chute = int(input(f"Digite o seu chute (0 a {sorteio_max}):"))
        if chute == numero:
            print("Parabéns, você é o bonzão mesmo")
            errou = False
            break
        else:
            print("Errou :c")  
            if chute < numero:
                print("Dica: o número secreto é MAIOR")
            else:
                print("Dica: o número secreto é MENOR")
        print("-" * 25)
        tentativas = tentativas + 1
       
    if errou == True:
        print("O número sorteado era:", numero) # mostra p quem errou
    print("### FIM DO JOGO ###")