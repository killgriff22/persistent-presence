from config import *
import os,time,subprocess,sys,random,asyncio
version = sys.version_info
print(f'Python version: {version.major}.{version.minor}.{version.micro}')
exit()
try:
    import discord
    from discord.ext import tasks
except ImportError:
    os.system('pip install discord.py-self')
    #determine python version by looking at "bin"
    version = sys.executable.split('/')[-1]

    import discord
    from discord.ext import tasks

user = discord.Client()