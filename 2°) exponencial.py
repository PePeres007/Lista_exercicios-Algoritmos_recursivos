def ler_expoente(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            n = int(entrada)
            if n >= 0:
                return n
            else:
                print("Digite apenas um número inteiro maior ou igual a zero!")
        except ValueError:
            print("Valor inválido! Por favor, digite um número inteiro.")

def ler_base(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            a = int(entrada)
            return a
        except ValueError:
            print("Valor inválido! Por favor, digite um número válido.")

def exponencial(a, n):
    if a == 0 and n == 0:
        return "Impossível calcular 0 **0"
    elif n == 0:
        return 1
    else:
        return a * exponencial(a, n - 1)

a = ler_base("Digite o número que irá ser a base: ")
n = ler_expoente("Digite o número que irá ser o expoente: ")
print(exponencial(a, n))
