from random import randint
from modules.data_classes.text_data import TextData
from modules.data_classes.globals import Globals

def handle(event):
    _data = TextData(event)
    _data.keys = ["cat"]

    default_mod = Globals.default_mod
    def send_message(msg, id):
        _vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, _data.int32_max)
        )
        print('Sending message "{}" to {} with id {}'.format(msg,
              "USER" if _data.event.object.peer_id == _data.event.object.from_id else "CHAT", id))

    if default_mod == __name__ and _data.string:
        send_message(_data.string, _data.event.object.peer_id)

    elif _data.command in _data.keys and _data.text:
        send_message(_data.text, _data.event.object.peer_id)

def init(vk_api):
    global _vk
    global _data

    _vk = vk_api