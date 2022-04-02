import math
import random

def metodoBisseccao():
    valor_a = float(input('Digite o valor de a: '))
    valor_b = float(input('Digite o valor de b: '))
    precisao_erro = float(input('Digite o valor da precisão de erro: '))
    total_iteracao = 1
    it = 0
    if(valor_b - valor_a) < precisao_erro:
        valor_x = random.uniform(valor_a, valor_b)
        print(f'A raiz encontrada foi x = {valor_x}')
    
    valor_m = f(valor_a)

    while (valor_b - valor_a) >= precisao_erro:
        valor_x = (valor_a + valor_b) / 2
        
        print(f'Iteração {it}: {valor_x}')
        it = it + 1
        if(valor_m * f(valor_x) > 0):
            valor_a = valor_x
            valor_subtracao = valor_b - valor_a
            if valor_subtracao < precisao_erro: 
                valor_x = random.uniform(valor_a, valor_b)
        else: 
            valor_b = valor_x
            total_iteracao = total_iteracao + 1

    print(f'A raiz encontrada foi x = {valor_x}')

def f(x):
    # return x * math.log(x) - 1 
    # return pow(x, 3) - 7 * pow(x, 2) + 14 * x - 6
    # return pow(x, 4) - 2 * pow(x, 3) - 4 * pow(x , 2) + 4 * x + 4
    return x - 2 * pow(2, -x)
metodoBisseccao()