import importlib, importlib.util
import os

from modules.data_classes.globals import Globals
from static.path_extra import remove_ext


class ModulesManager:
    """
    Class for importing modules and handling events with them
    Args:
        vk_api (:obj:`vk_api`): instance of `vk_api` for working with api
        path (str): path to folder with python (.py) modules
            Default value of `path` is path to current script and its
            `modules` subfolder
    """

    def __init__(self, vk_api, path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules")):
        self.path = path
        files = os.listdir(self.path)
        scripts = [f for f in files if f.endswith(".py")]

        self._persistent_mods_list = [
            "globals_manager"
        ]

        self._modules = {}
        self._persistent_mods = {}
        for script_name in scripts:
            mod = self._import_module_from_file(script_name)
            if mod:
                mod.init(vk_api)
                no_ext = remove_ext(script_name)

                if no_ext in self._persistent_mods_list:
                    self._persistent_mods[no_ext] = mod
                else:
                    self._modules[no_ext] = mod

    def _import_module_from_file(self, module_name):
        """
        Imports python script from file and gives access to its functions
        :param module_name: name of python script including extension
        :return: loaded module or None (if couldn't succeed)
        """
        module_dir = os.path.join(self.path, module_name)
        module_name = module_name[:module_name.rfind('.')]

        module_spec = importlib.util.spec_from_file_location(
            module_name,
            module_dir
        )

        # Check if module specification is correct
        if module_spec:
            mod = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(mod)
            return mod
        else:
            print('Could not find module "{}" in directory "{}"'.format(module_name, self.path))
            return None

    def handle(self, event):
        """
        Executes `handle` function for each module or for the specific
        module specified in the 'default_mod' variable and persistent modules.
        Args:
            event (:obj:`vk_api.bot_longpoll.VkBotMessageEvent`): received message
        """

        default_mod = Globals.default_mod
        try:
            for mod in self._persistent_mods.values():
                mod.handle(event)

            if Globals.default_mod == '':
                for mod in self._modules.values():
                    mod.handle(event)
            else:
                self._modules[default_mod].handle(event)

        except (KeyError, AttributeError):
            print('Could not execute "handle" for module "{}"'.format(default_mod))
