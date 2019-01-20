import time
from modules.data_classes.text_data import TextData

def handle(event):
    data = TextData(event)
    data.keys = ["sleep"]
    max_sleep_value = 10

    if len(data.text) > 2:
        val = data.text[:3]
    else:
        val = data.text

    if data.command in data.keys:
        try:
            value = int(val)
            value = abs(value)
            if value > max_sleep_value:
                value = max_sleep_value
            print('Sleeping for {} seconds, command by {} with id {}'.format(value, "USER" if data.event.object.peer_id == data.event.object.from_id else "CHAT", data.id))
            time.sleep(value)

        except ValueError:
            print('Failed to convert message "{}" from {} with id {} to int.'.format(data.text, "USER" if data.id == data.event.object.from_id else "CHAT", id))

def init(vk_api):
    global _data
