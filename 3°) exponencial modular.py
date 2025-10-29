def ler_inteiro(mensagem, condicao=None, msg_erro="Valor inválido!"):
    while True:
        entrada = input(mensagem)
        try:
            n = int(entrada)
            if condicao is None or condicao(n):
                return n
            else:
                print(msg_erro)
        except ValueError:
            print("Digite apenas um número inteiro.")

def exponencial_modular(a, n, m):
    if m == 1:
        return "Impossível calcular: módulo igual a 1."
    if a == 0 and n == 0:
        return (f"Impossível calcular: caso 0^0 mod {m}.")
    if n == 0:
        return 1 % m
    else:
        return (a * exponencial_modular(a, n - 1, m)) % m

a = ler_inteiro("Digite o valor da base (a): ")
n = ler_inteiro("Digite o valor do expoente inteiro (n ≥ 0): ", condicao=lambda x: x >= 0, 
                msg_erro="O expoente deve ser inteiro e ≥ 0")
m = ler_inteiro("Digite o valor do módulo (m ≥ 2): ", condicao=lambda x: x >= 2, 
                msg_erro="O módulo deve ser inteiro e ≥ 2")

resultado = exponencial_modular(a, n, m)
print(f"O resultado de {a}^{n} mod {m} é: {resultado}")
