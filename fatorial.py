def fatorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

n = int(input("Digite o número que deseja ver o fatorial: "))
print(fatorial(n))
