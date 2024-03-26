from config import *
import os
import time
import subprocess
import sys
import random
import asyncio
version = sys.version_info
version = (f'python{version.major}.{version.minor}')
old1474 = """        build_url = 'https://discord.com/assets/' + re.compile(r'assets/+([a-z0-9]+)\.js').findall(login_page)[-2] + '.js'\n"""
old1478 = """        return int(build_file[build_index : build_index + 6])\n"""
new1474 = """        build_url = 'https://discord.com/assets/' + re.compile(r'assets/+([a-z0-9]+)').findall(login_page)[-2] + '.js'\n"""
new1478 = """        return (build_file[build_index : build_index + 6])\n"""
try:
    import discord
    from discord.ext import tasks
except ImportError:
    os.system('pip install discord.py-self')
    import discord
    from discord.ext import tasks

user = discord.Client()
