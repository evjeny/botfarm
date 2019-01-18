from random import randint
from commands.DataClasses.TextData import TextData

def Main(event, vk_session, vk):
    data = TextData(event, vk_session, vk)
    data.catmode = False # Значение устанавливается вручную
    data.keys = ["cat"]

    def parse_message(data):
        # print(self.event.object)
        if data.catmode:
            send_message(data, data.string, data.event.object.peer_id)
        else:
            send_message(data, data.text, data.event.object.peer_id)

    def send_message(data, msg, id):
        data.vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, data.int32_max)
        )
        print('Sending message "{0}" to {1} with id {2}'.format(msg, "USER" if data.event.object.peer_id == data.event.object.from_id else "CHAT", id))


    if data.catmode or data.command in data.keys:
        parse_message(data)
