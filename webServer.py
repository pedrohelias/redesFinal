import asyncio
import websockets

clients = set()

async def register(websocket):

    clients.add(websocket)
    #print(f"Novo cliente conectado. Total de clientes: {len(clients)}")
    print(f"Novo cliente conectado")

async def unregister(websocket):
    clients.remove(websocket)
    print(f"Cliente desconectado")

async def chat(websocket, path):

    await register(websocket)
    try:
        async for message in websocket:
            await asyncio.gather(
                *[client.send(message) for client in clients if client != websocket]
            )
    finally:
        await unregister(websocket)

start_server = websockets.serve(chat, "localhost", 12345)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
