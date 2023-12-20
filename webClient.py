import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        message = input("digite a mensagem: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
