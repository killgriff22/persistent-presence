from config import *
import os,time,subprocess,sys,random,asyncio
print(sys.executable)
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