from functions import *
try:
    user.run(TOKEN)
except IndexError:
    with open(f"lib/{version}/site-packages/discord/utils.py", "r+") as f:
        lines = f.readlines()
        print(lines[1473])
