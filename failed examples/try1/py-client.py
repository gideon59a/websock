# Ref: https://www.youtube.com/watch?v=tgtb9iucOts
import websockets
import asyncio

async def listen():
    #url = "ws://simple-websocket-server-echo.glitch.me"
    url = "ws://192.168.1.211:50001"
    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())