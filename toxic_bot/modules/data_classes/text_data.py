class TextData:
    def __init__(self, event):
        self.int32_max = 2147483647
        self.keys = []

        self.event = event
        self.id = event.object.peer_id
        self.string = self.event.object.text

        temp = self.string.find(' ')
        if temp == -1:
            self.command = self.string
            self.text = ''
        else:
            self.command = self.string[:temp]
            self.text = self.string[temp + 1:]
        self.command = self.command.lower()
