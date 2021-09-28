import asyncio
import socketio
import aioconsole

sio = socketio.AsyncClient(logger=True, engineio_logger=True)  # (logger=True, engineio_logger=True)

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def srv_message(data):
    print('message received from server with ', data)
    print('send response')
    await sio.emit('client_response', {'cl2 response': 'my response'})
    return "OK", 123

@sio.event
async def disconnect():
    print('disconnected from server')

async def my_background_task(my_argument):
    # do some background work here!
    for i in range(my_argument):
        await sio.sleep(5)  # (rather than asyncio.sleep(5) ...?)
        await sio.emit('client_response', {'background emits': 'stam'})


async def kb_echo_to_server(num):
    # ref: https://stackoverflow.com/questions/35223896/listen-to-keypress-with-asyncio
    for i in range(num):
        kb_input = await aioconsole.ainput('enter something: ')
        print(f'kb_input:  {kb_input}')
        await sio.emit('client_response', {'from keyborad': kb_input})


async def main():
    await sio.connect('http://localhost:5003')

    task = sio.start_background_task(my_background_task, 2)
    await task

    task2 = sio.start_background_task(kb_echo_to_server, 5)
    await task2

    await sio.wait()



if __name__ == '__main__':
    asyncio.run(main())
