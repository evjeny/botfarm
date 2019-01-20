from random import randint
from modules.data_classes.text_data import TextData


def handle(event):
    _data = TextData(event)
    _data.keys = ["cat"]

    def send_message(msg, id):
        _vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, _data.int32_max)
        )
        print('Sending message "{0}" to {1} with id {2}'.format(msg,
            "USER" if _data.event.object.peer_id == _data.event.object.from_id else "CHAT", id))

    if _data.command in _data.keys:
        send_message(_data.text, _data.event.object.peer_id)


def init(vk_api):
    global _vk
    global _data

    _vk = vk_api