from config import *
import os
import time
import subprocess
import sys
import random
import asyncio
version = sys.version_info
version = (f'python{version.major}.{version.minor}')
try:
    import discord
    from discord.ext import tasks
except ImportError:
    os.system('pip install discord.py-self')
    import discord
    from discord.ext import tasks

user = discord.Client()
