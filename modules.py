from config import *
import os,time,subprocess,sys,random,asyncio
try:
    import discord
    from discord.ext import tasks
except ImportError:
    os.system('pip install discord')
    import discord
    from discord.ext import tasks

user = discord.Client()