import vk_api
import json
from ImportManager import ImportManager
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class VKbot:
    def __init__(self, token, group_id):
        self.random_id = 0
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()

        self.longpoll = VkBotLongPoll(self.vk_session, group_id)
        self.import_commands()

    """Слушаем все events в longpoll"""
    def listen_for_longpoll(self):

        print("Started listening")
        print()

        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.object.text:
                self.event = event
                self.check_for_commands()

    """Исполняет метод Main в каждой команде"""
    def check_for_commands(self):
        for elem in self.commands:
            elem.Main(self.event, self.vk_session, self.vk)

    """Импорт всех команд из папки commands"""
    def import_commands(self):
        import_manager = ImportManager()
        self.commands = import_manager.get_all_commands()


with open("login_data.json", "r") as file:
    data = json.loads(file.read())
    token = data["token"]
    group_id = data["group_id"]

vk = VKbot(token, group_id)
vk.listen_for_longpoll()
