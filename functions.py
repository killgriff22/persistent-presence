from classes import *

@user.event
async def on_ready():
    print('------')
    print(f'Logged in as {user.user.name} ({user.user.id})')
    print('------')
