def ler_inteiro(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            n = int(entrada)
            return n
        except ValueError:
            print("Digite apenas um número inteiro.")

def mdc(a, b):
    if a == 0 and b == 0:
        return "mdc indeterminado!"
    elif b == 0:
       return abs(a) 
    else:
        return mdc(b, a % b)

a = ler_inteiro("Digite o primeiro número inteiro (a): ")
b = ler_inteiro("Digite o segundo número inteiro (b): ")

resultado = mdc(a, b)
print(f"O mdc de {a} e {b} é: {resultado}")
