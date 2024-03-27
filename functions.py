from classes import *

@user.event
async def on_ready():
    print('------')
    print(f'Logged in as {user.user.name} ({user.user.id})')
    print('------')

@user.command('set')
async def set(ctx, *, activity: str, type: str,url: str = ''):
    if type == 'listening':
        await user.change_presence(activity=Custom_Activities.listening(name=activity))
    elif type == 'playing':
        await user.change_presence(activity=discord.Game(name=activity))
    elif type == 'streaming':
        await user.change_presence(activity=discord.Streaming(name=activity, url='https://www.twitch.tv/'))
    elif type == 'watching':
        await user.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
    else:
        await ctx.send('Invalid activity type')