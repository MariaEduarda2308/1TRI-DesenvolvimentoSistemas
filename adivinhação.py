import random
def jogar():
    print("Fácil = 5 tentativas")
    print("Médio = 3 tentativas")
    print("Díficil = 1 tentativa")
    opcao = int(input("Digite a opção desejada (1 a 3)"))

    if opcao == 1:
        print("Selecionado opção 1")
        sorteio_max = 10  # número entre 0 e 10
        tentativas_max = 5
    elif opcao == 2:
        print("Selecionado opção 2")
        sorteio_max = 10  # número entre 0 e 10
        tentativas_max = 3
    elif opcao == 3:
        print("Selecionado opção 3")
        sorteio_max = 10  # número entre 0 e 10
        tentativas_max = 1
    else:
        print("Opção inválida, digite um número de 1 a 3")

    tentativas = 1
    errou = True

    numero = random.randint(0, sorteio_max)  # sorteio correto entre 0 e 10

    while (tentativas <= tentativas_max):
        print("Tentativa:", tentativas)
        chute = int(input("Digite o seu chute (0 a 10):"))
        if chute == numero:
            print("Parabéns, você é o bonzão mesmo")
            errou = False
            break
        else:
            print("Errou :c")
            if numero > chute:
                print("O número é maior que a tentativa")
            else:
                print("Número menor que a tentativa")
        tentativas = tentativas + 1

    if errou == True:
        print("O número sorteado era:", numero)
    print("FIM DO JOGO")
