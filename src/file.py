import io
from fun import *

# The file class
class File:
    def __init__(self, location):
        self.location = location

        self.raw = self.getRaw()
        self.name = self.getName()

    def getRaw(self):
        # Opens file in UTF - 8
        openFile = io.open(self.location, mode='r', encoding='utf-8')
        content = openFile.readlines()

        return content

    def getName(self):
        dirs = self.location.split('/')
        nameWithExt = dirs[-1:][0]
        name = nameWithExt.split('.')[0]

        return name

    def __repr__(self):
        repr = '\n'
        repr += 'NAME:' + self.name + '\n'
        repr += 'LOCATION:' + self.location + '\n\n\n'

        return repr
