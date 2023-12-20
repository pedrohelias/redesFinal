import asyncio
import websockets

# Lista para armazenar as conexões dos clientes
clients = set()

async def register(websocket):
    # Adiciona a conexão do cliente à lista
    clients.add(websocket)
    #print(f"Novo cliente conectado. Total de clientes: {len(clients)}")
    print(f"Novo cliente conectado")

async def unregister(websocket):
    # Remove a conexão do cliente da lista
    clients.remove(websocket)
    #print(f"Cliente desconectado. Total de clientes: {len(clients)}")
    print(f"Cliente desconectado")

async def chat(websocket, path):
    # Registra o novo cliente
    await register(websocket)
    try:
        # Aguarda mensagens do cliente
        async for message in websocket:
            # Envia a mensagem para todos os clientes conectados
            await asyncio.gather(
                *[client.send(message) for client in clients if client != websocket]
            )
    finally:
        # Remove o cliente da lista ao desconectar
        await unregister(websocket)

start_server = websockets.serve(chat, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
