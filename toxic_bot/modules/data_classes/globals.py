import os


class Globals:
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(path)

    files = os.listdir(path)
    mods_list = [f[:-3] for f in files if f.endswith(".py")]
    if len(mods_list) == 0:
        mods_list.append("No modules found")

    valid_default_mods = [
        "cat"
    ]
    default_mod = ''

