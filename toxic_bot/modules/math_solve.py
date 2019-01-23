import sympy

from sympy import S
from random import randint

import static.math_parser as math_parser
from modules.data_classes.text_data import TextData

def handle(event):
    def send_message(msg, id):
        _vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, _data.int32_max)
        )
        print('Sending message "{}" to {} with id {}'.format(msg,
              "USER" if _data.event.object.peer_id == _data.event.object.from_id else "CHAT", id))

    _data = TextData(event)
    _data.keys = ["solve"]

    if _data.command in _data.keys:
        equation, sym = math_parser.parse(_data.text)
        if sym:
            try:
                res = sympy.solveset(equation, sym, S.Reals)
                if type(res) is sympy.EmptySet:
                    send_message("No solutions found", _data.id)
                else:
                    msg = "Solution: {}".format(', '.join([str(i) for i in res]))
                    send_message(msg, _data.id)

            except ValueError:
                send_message("Unable to solve the equation", _data.id)

        else:
            send_message("Result: {}".format(equation), _data.id)


def init(vk_api):
    global _vk
    global _data

    _vk = vk_api