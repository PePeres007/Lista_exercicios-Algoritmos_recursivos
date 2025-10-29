def ler_inteiro():
    while True:
        entrada = input("Digite um número inteiro: ")
        try:
            n = int(entrada)
            return n
        except ValueError:
            print("Valor inválido! Por favor, digite apenas um número inteiro.")

def fatorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = ler_inteiro()
print(fatorial(n))
