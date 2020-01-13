class MyUser:
    def __init__(self):
        self.text = ''
        self.error = ''

    def input(self, keyPressed):
        if 'a' <= keyPressed.lower() and 'z' >= keyPressed.lower():
            self.text += keyPressed
            self.error = ''

        elif keyPressed == ' ':
            self.error = 'Nospace allowed'

        elif keyPressed == '\r':
            if len(self.text) >= 4:
                self.error = ''
            else:
                self.error = 'minimum lenght is 4 characters'
        else:
            self.error = 'invalid character ' + keyPressed

    def delete(self):
        self.text = self.text[0:-1]

    def get(self):
        return self.text

    def __len__(self):
        return self.text.__len__()


USERNAME = MyUser()
