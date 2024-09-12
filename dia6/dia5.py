def fatorial(num):
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado
    
def main():
    num = int(input("Insira um valor inteiro positivo: "))
    
    if num < 0:
        print("Erro: O numero precisa ser um inteiro positivo.")
    else:
        resultado = fatorial(num)
        print(f"O fatorial de {num} é {resultado}")
        
if __name__ == '__main__':
    main()