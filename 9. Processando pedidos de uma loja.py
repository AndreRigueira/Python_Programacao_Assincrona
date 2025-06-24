"""
Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. 
O sistema deve seguir a seguinte lógica:

Primeiro, verificar se o pagamento foi aprovado;
Se o pagamento for aprovado, verificar se há estoque disponível;
Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.
A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confira o código:

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.

Saída esperada:

Processando pedido #101...
Pagamento aprovado para pedido #101.
Estoque disponível para pedido #101.
Pedido #101 confirmado! Enviado para entrega.
 
Processando pedido #102...
Pagamento aprovado para pedido #102.
Estoque indisponível para pedido #102. Pedido cancelado.
 
Processando pedido #103...
Pagamento recusado para pedido #103. Pedido cancelado.
 
Todos os pedidos foram processados!
"""
import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def processa_pedido(id):
    for pedido_atual in pedidos:
        if pedido_atual['id'] == id:
            #print(f'Id = {pedido_atual['id']} | Pagamento aprovado? {pedido_atual['pagamento_aprovado']} | Em estoque? {pedido_atual['estoque_disponivel']}')
            print(f'Processando pedido {pedido_atual['id']}...')
            if pedido_atual['pagamento_aprovado']:
                print(f'Pagamento aprovado para pedido {pedido_atual['id']}.')
                if pedido_atual['estoque_disponivel']:
                    print(f'Estoque disponível para pedido {pedido_atual['id']}.')
                    print(f'Pedido {pedido_atual['id']} confirmado! Enviado para entrega.\n')
                else:
                    print(f'Estoque indisponível para pedido {pedido_atual['id']}. Pedido cancelado.\n')
            else:
                print(f'Pagamento recusado para pedido {pedido_atual['id']}. Pedido cancelado.\n')
            break


async def main():
    await asyncio.gather(
        processa_pedido(101),
        processa_pedido(102),
        processa_pedido(103)
    )

asyncio.run(main())
        
