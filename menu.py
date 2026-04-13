import adivinhacao
import forca
while True:
    print("\n" + "-"*40)
    print("       ESCOLHA O JOGO")
    print("-"*40)
    print("1 - Jogar Adivinhação")
    print("2 - Jogar Forca ")
    print("0 - Sair")
    opcao = input("Digite sua opção: ").strip()


    if opcao == "0":
        print("Até a próxima!")
        break
    elif opcao == "1":
        adivinhacao.jogar()

    elif opcao == "2":
        forca.jogar()

    else:
        print("Opção inválida") 