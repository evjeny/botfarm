import importlib, importlib.util
import os

class ImportManager:
    def __init__(self):
        self.this_dir = os.path.dirname(os.path.abspath(__file__)) + "/commands"
        files = os.listdir(self.this_dir)
        self.scripts = [f for f in files if f.endswith(".py")]
        self.modules = []

    """Перебирает все модули в директории и импортирует их.
    Возвращает список модулей.
    """
    def get_all_commands(self):
        for full_name in self.scripts:
            mod = self._import_module_from_file(full_name)
            self.modules.append(mod)
        return self.modules

    """Импортирует модуль из переданной директории"""
    def _import_module_from_file(self, full_name):
        module_dir = self.this_dir + "/" + full_name
        module_name = full_name[:full_name.rfind('.')]

        # Получение спецификации модуля.
        module_spec = importlib.util.spec_from_file_location(
            module_name,
            module_dir
        )
        # Импортирование модуля по спецификации.
        if module_spec:
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            return module
        else:
            print('Could not find module "{}" in directory "{}"'.format(module_name, self.this_dir))
            return None
