import importlib, importlib.util
import os


class ModulesManager:
    """
    Class for importing modules and handling events with them
    Args:
        vk_api (:obj:`vk_api`): instance of `vk_api` for working with api
        path (str): Path to folder with python (.py) modules
            Default value of `path` is path to current script and it's
            `modules` subfolder
    """

    def __init__(self, vk_api, path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules")):
        self.path = path
        files = os.listdir(self.path)
        scripts = [f for f in files if f.endswith(".py")]

        self._modules = []
        for script_name in scripts:
            mod = self._import_module_from_file(script_name)
            if mod:
                mod.init(vk_api)
                self._modules.append(mod)

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
        Executes `handle` function for each module
        Args:
            event (:obj:`vk_api.bot_longpoll.VkBotMessageEvent`): received message
        """
        for mod in self._modules:
            mod.handle(event)
