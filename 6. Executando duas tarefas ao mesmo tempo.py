"""
Carlos é um engenheiro de software que precisa processar duas tarefas simultaneamente: uma que simula um download e outra que simula uma análise de dados. 
Ele quer que ambas as tarefas sejam iniciadas ao mesmo tempo, e que o programa exiba mensagens informando o início e o fim de cada uma.

Com base nesse cenário, crie um programa que inicie ambas as tarefas ao mesmo tempo, e exiba as mensagens quando cada uma for concluída. 
Dica: Utilize asyncio.gather() para rodar ambas em paralelo.

Saída esperada:

Iniciando download... 
Iniciando análise de dados... 
Download concluído! 
Análise de dados concluída! 

"""

import asyncio

async def download():
    print('Iniciando download...')
    await asyncio.sleep(3)
    print('Download concluído!')

async def analise():   
    print('Iniciando análise de dados...')
    await asyncio.sleep(1)
    print('Análise de dados concluída!')

async def main():
    await asyncio.gather(
        download(),
        analise()
    )

asyncio.run(main())