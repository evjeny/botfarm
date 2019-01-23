import time
from modules.data_classes.text_data import TextData

def handle(event):
    _data = TextData(event)
    _data.keys = ["sleep"]
    max_sleep_value = 10

    if len(_data.text) > 2:
        val = _data.text[:3]
    else:
        val = _data.text

    if _data.command in _data.keys:
        try:
            value = int(val)
            value = abs(value)
            if value > max_sleep_value:
                value = max_sleep_value
            print('Sleeping for {} seconds, command by {} with id {}'.format(value, "USER"
                  if _data.event.object.peer_id == _data.event.object.from_id else "CHAT", _data.id))
            time.sleep(value)

        except ValueError:
            print('Failed to convert message "{}" from {} with id {} to int.'.format(_data.text, "USER"
                  if _data.id == _data.event.object.from_id else "CHAT", _data.id))

def init(vk_api):
    global _data
