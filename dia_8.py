
def tabuada(numero):
    multiplicado = 0
    while multiplicado < 10:
        multiplicado += 1
        calculo = numero * multiplicado
        resultado = print(f'{numero} X {multiplicado} = {calculo}')   
        
    return resultado


numero = int(input('Digite um numero inteiro: '))

tabuada(numero)
