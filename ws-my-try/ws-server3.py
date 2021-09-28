# WS server example
# REF: https://websockets.readthedocs.io/en/stable/intro/index.html
#      (pointed by: https://websockets.readthedocs.io/en/stable/)

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
