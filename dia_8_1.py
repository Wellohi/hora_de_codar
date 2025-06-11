def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fatorial(n-1)
        
num = int(input("Digite um numero inteiro: "))

if num >= 0:
    resultado = fatorial(num)
    print(f'Fatorial de {num} é {resultado}')
else:
    print('Número inválido')