def tabuada(opcao, num):
    if opcao == 1:
        for i in range(0, 11):
            print(f"{num} + {i} = {num + i}")
    elif opcao == 2:
        for i in range(0, 11):
            print(f"{num} - {i} = {num - i}")
    elif opcao == 3:
        for i in range(0, 11):
            print(f"{num} * {i} = {num * i}")
    elif opcao == 4:
        for i in range(1, 11):  # Evitar divisão por 0
            print(f"{num} / {i} = {num / i:.2f}")

def menu():
    print(
        """
    Tabuada
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisao
    [0] Sair
        """
    )

def main():
    opcao = -1
    while opcao != 0:
        menu()
        opcao = int(input("Insira a opção correspondente: "))

        if opcao == 0:
            print("Saindo ...")
            break

        if opcao < 1 or opcao > 4:
            print("Opção inválida!")
            continue

        num = int(input("Insira um valor: "))
        tabuada(opcao, num)

        continuar = input("Deseja continuar? Digite S ou N.\n").lower()
        if continuar != 's':
            print("Saindo ...")
            break

if __name__ == "__main__":
    main()
