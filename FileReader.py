
class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        with open(self.fileName, 'r') as myfile:
            template = myfile.read()
            return template



