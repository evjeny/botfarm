from random import randint

from modules.data_classes.text_data import TextData
from modules.data_classes.globals import Globals

def handle(event):
    _data = TextData(event)
    _data.keys = [
        "defaultmodule",
        "modules",
        "all_modules",
        "reset"
    ]
    valid_mods = Globals.valid_default_mods

    def send_message(msg, id):
        _vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, _data.int32_max)
        )
        print('Sending message "{}" to {} with id {}'.format(msg,
              "USER" if _data.event.object.peer_id == _data.event.object.from_id else "CHAT", id))

    if _data.command == _data.keys[0]:
        if _data.text in valid_mods:
            Globals.default_mod = _data.text
            send_message('Successfully set "{}" as the default module'.format(_data.text), _data.id)
        else:
            send_message('Could not find module "{}"'.format(_data.text), _data.id)

    elif _data.command == _data.keys[1]:
        temp = 'Valid modules for "defaultmod":\n'
        send_message(temp + ', '.join(valid_mods), _data.id)

    elif _data.command == _data.keys[2]:
        send_message(', '.join(Globals.mods_list), _data.id)

    elif _data.command == _data.keys[3]:
        if Globals.default_mod != '':
            Globals.default_mod = ''
            send_message("Successfully reseted the default module", _data.id)
        else:
            send_message("There is no default module right now", _data.id)


def init(vk_api):
    global _vk
    global _data

    _vk = vk_api