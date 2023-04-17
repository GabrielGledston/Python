num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("O número deve ser positivo.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    print("O fatorial de", num, "é", fatorial)
