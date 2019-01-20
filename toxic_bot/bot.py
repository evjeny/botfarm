import json

from modules_manager import ModulesManager

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class ToxicBot:
    def __init__(self, token, group_id):
        self.random_id = 0
        self.vk_session = vk_api.VkApi(token=token)
        self.vk = self.vk_session.get_api()

        self.longpoll = VkBotLongPoll(self.vk_session, group_id)
        self.module_manager = ModulesManager(self.vk)

        self.listen_for_longpoll()

    def listen_for_longpoll(self):
        print("Started listening\n")

        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.object.text:
                self.module_manager.handle(event)


if __name__ == "__main__":
    with open("login_data.json", "r") as file:
        data = json.loads(file.read())
        token = data["token"]
        group_id = data["group_id"]

    bot = ToxicBot(token, group_id)
