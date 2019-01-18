import time
from commands.DataClasses.TextData import TextData

def Main(event, vk_session, vk):
    data = TextData(event, vk_session, vk)
    data.keys = ["sleep"]

    if len(data.text) > 2:
        val = data.text[:3]
    else:
        val = data.text
    
    if data.command in data.keys:
        try:
            value = int(val)
        except ValueError:
            print('Failed to convert message "{0}" from {1} with id {2} to int.'.format(msg, "USER" if data.event.object.peer_id == data.event.object.from_id else "CHAT", id))
            
    value = abs(value)
    if value > 10:
        value = 10
    time.sleep(value)
