from random import randint
import pickle
import re

from numpy.random import choice

from commands.DataClasses.TextData import TextData


def Main(event, vk_session, vk):
    def read_words(filename):
        try:
            with open(filename, 'rb') as handle:
                return pickle.load(handle)
        except FileNotFoundError:
            return dict()

    def save_words(words, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(words, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def send_message(data, msg, id):
        data.vk.messages.send(
            peer_id=id,
            message=msg,
            random_id=randint(0, data.int32_max)
        )
        print('Sending message "{0}" to {1} with id {2}'.format(msg,
            "USER" if data.event.object.peer_id == data.event.object.from_id else "CHAT", id))

    def add_to_stats(words, data):
        text = data.string.lower()
        parts = re.split("[\W_\d]+", text)
        parts.append(".")

        prev = ""
        for i, part in enumerate(parts):
            next_words = words.get(prev, dict())
            next_words[part] = next_words.get(part, 0) + 1
            words[prev] = next_words

            prev = part

    def get_next_word(words, current_word):
        vars = words.get(current_word, {".": 1})
        all_variants = sum(vars.values())
        for k, v in vars.items():
            vars[k] = v / all_variants
        word = choice(list(vars.keys()), p=list(vars.values()))
        return word

    def generate_words(words, limit, data):
        current_word = get_next_word(words, "")
        res = [current_word]
        i = 1
        while i < limit and current_word != ".":
            res.append(get_next_word(words, current_word))
            i += 1
        return " ".join(res)

    data_file = 'words.mchain'
    words = read_words(data_file)

    data = TextData(event, vk_session, vk)
    data.keys = ["speak"]

    if data.command in data.keys:
        try:
            limit = int(data.text)
        except ValueError:
            limit = 20
        text = generate_words(words, limit, data)
        text = text[:min(4096, len(text))]
        send_message(data, text, data.event.object.peer_id)
    else:
        add_to_stats(words, data)
        save_words(words, data_file)
