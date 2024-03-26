from functions import *
try:
    user.run(TOKEN)
except IndexError: #Patch discord.py-self to bypass shitty code
    f = open(f"lib/{version}/site-packages/discord/utils.py", "r")
    lines = f.readlines()
    f.close()
    os.remove(f"lib/{version}/site-packages/discord/utils.py")
    print(f"old lines: line 1474: {lines[1473] == old1474}, line 1478: {lines[1477] == old1478}")
    if lines[1473] == new1474 and lines[1478] == new1478:
        print("Already patched")
        exit()
    lines[1473] = "        build_url = 'https://discord.com/assets/' + re.compile(r'assets/+([a-z0-9]+)').findall(login_page)[-2] + '.js'\n"
    lines[1477] = "        return (build_file[build_index : build_index + 6])\n"
    print(f"new lines: line 1474: {lines[1473] == new1474}, line 1478: {lines[1477] == new1478}")
    if lines[1473] == new1474 and lines[1477] == new1478:
        print("Patched: Check 1")
    f = open(f"lib/{version}/site-packages/discord/utils.py", "w")
    f.write("".join(lines))
    f.close()
    f = open(f"lib/{version}/site-packages/discord/utils.py", "r")
    lines = f.readlines()
    f.close()
    print(f"new lines: line 1474: {lines[1473] == new1474}, line 1478: {lines[1477] == new1478}")
    if lines[1473] == new1474 and lines[1477] == new1478:
        print("Patched: Check 2")
    else:
        print("Failed to patch, uninstalling")
        os.system(f"pip uninstall discord.py-self -y")