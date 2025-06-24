"""
Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. 
Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, e os resultados exibidos assim que estiverem prontos.

Crie um programa que calcule o fatorial de cinco números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente 
e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.

Dica: use a função sleep para simular um tempo de processamento.

Dica: para testar o funcionamento do seu código, utilize uma lista de números em ordem de tamanho aleatória. Exemplo: numeros = [5, 3, 7, 4, 6]

Saída esperada:

Fatorial de 3 = 6
Fatorial de 4 = 24
Fatorial de 5 = 120
Fatorial de 6 = 720
Fatorial de 7 = 5040

"""
import asyncio, math

async def fatorial(num,tempo):
    #print(f'Fatorial de {num} iniciado.')
    await asyncio.sleep(tempo)
    '''
    # Cálculo de fatorial usando o laço 'for'
    resultado = 1
    for n in range(1,num+1):
        resultado *= n
    print(f'Fatorial de {num} = {resultado}')
    '''
    # Calculo de fatorial usando a lib 'math'
    print(f'Fatorial de {num} = {math.factorial(num)}')

async def main():
    await asyncio.gather(
        fatorial(5,4),
        fatorial(3,2),
        fatorial(7,6),
        fatorial(4,3),
        fatorial(6,5)
    )

asyncio.run(main())