from random import randint
from modules.data_classes.text_data import TextData


def handle(event):
    data = TextData(event)
    data.keys = ["my_id", "peer_id"]

    def send_message(data, msg, id):
        _vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, data.int32_max)
        )
        print('Sending message "{0}" to {1} with id {2}'.format(msg,
            "USER" if data.event.object.peer_id == data.event.object.from_id else "CHAT", id))

    if data.command == data.keys[0]:
        send_message(data, data.event.object.from_id, data.id)
    elif data.command == data.keys[1]:
        send_message(data, data.id, data.id)


def init(vk_api):
    global _vk
    global _data

    _vk = vk_api