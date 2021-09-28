#XX#!/usr/bin/env python

# Ref: https://websockets.readthedocs.io/en/stable/

import asyncio
import websockets

async def hello():
    print("before connecting")
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected ???")
        await websocket.send("Hello world!")
        print("Sent ???")
        await websocket.recv()
        print("Received ???")

asyncio.run(hello())