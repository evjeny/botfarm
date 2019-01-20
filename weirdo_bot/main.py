import json

from modules_manager import ModulesManager

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def get_params(params_file):
    with open(params_file, "r") as file:
        data = json.loads(file.read())
        token = data["token"]
        group_id = data["group_id"]
        return token, group_id


if __name__ == '__main__':
    token, group_id = get_params("login_data.json")

    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, group_id=group_id)

    manager = ModulesManager(vk)

    print("bot started")

    for current_event in longpoll.listen():
        if current_event.type == VkBotEventType.MESSAGE_NEW and current_event.object.text:
            manager.handle(current_event)

