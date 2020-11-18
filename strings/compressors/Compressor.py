class Compressor:
    def __init__(self, text = ""):
        self.text = text

    def update(self, text = ""):
        self.text += text

    def compress(self):
        return self.text

    def write(self, filename = "out.txt"):
        pass

