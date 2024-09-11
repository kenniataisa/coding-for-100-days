def tabuada(opcao, num):

    if opcao == 1:
        for i in range(0,11):
            print(num, "+", i, "=", num + i)
    elif opcao == 2:
        for i in range(0,11):
            print(num, "-", i, "=", num - i)
    elif opcao == 3:
        for i in range(0,11):
            print(num, "x", i, "=", num * i)
    else:
        for i in range(1,11):
            print(num, "/", i, "=", num / i)

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

        num = int(input("Insira um valor: "))
        tabuada(opcao, num)

if __name__ == '__main__':
    main()




