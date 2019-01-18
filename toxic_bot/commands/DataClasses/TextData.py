class TextData:
    def __init__(self, event, vk_session, vk):
        self.catmode = False
        self.int32_max = 2147483647
        self.keys = []

        self.event = event
        self.id = event.object.peer_id
        self.vk = vk
        self.vk_session = vk_session
        self.string = self.event.object.text

        temp = self.string.find(' ')
        if temp == -1:
            self.command = self.string
        else:
            self.command = self.string[:temp]
        self.command = self.command.lower()

        self.text = self.string[temp+1:]
