#XX#!/usr/bin/env python

# Ref: https://websockets.readthedocs.io/en/stable/

import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())