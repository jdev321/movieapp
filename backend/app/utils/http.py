from aiohttp import ClientSession

CLIENT_SESSION: ClientSession

async def client_start():
    global CLIENT_SESSION
    CLIENT_SESSION = ClientSession()

async def client_end():
    global CLIENT_SESSION
    await CLIENT_SESSION.close()
