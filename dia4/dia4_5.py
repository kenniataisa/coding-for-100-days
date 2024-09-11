def tabuada(opcao, num1, num2):

    if opcao == 1:
        print(num1, "+", num2, "=", num1 + num2)
    elif opcao == 2:
        print(num1, "-", num2, "=", num1 - num2)
    elif opcao == 3:
        print(num1, "x", num2, "=", num1 * num2)
    elif opcao == 4:
        if num2 == 0:
            print("Divisão por zero não é permito!")
        else:
            print(num1, "/", num2, "=", num1 / num2)

def main():
    opcao = -1
    while opcao != 0:
        print(
            "[1] Soma\n"
            "[2] Subtração\n"
            "[3] Multiplicação\n"
            "[4] Divisao\n"
            "[0] Sair"
        )
        
        opcao = int(input("Insira a opção correspondente: "))

        if opcao == 0:
            print("Saindo...")
            break

        if opcao > 4 or opcao < 0:
            print("Opcao invalida")
            continue

        num1 = int(input("Insira o primeiro num1ero: "))
        num2 = int(input("Insira o primeiro num1ero: "))

        tabuada(opcao, num1, num2)

        continuar = input("Deseja continuar? Digite 'S' para SIM e 'N' para NÂO.\n").lower()

        if continuar != 's':
            print("Saindo ...")
            break

if __name__ == '__main__':
    main()




