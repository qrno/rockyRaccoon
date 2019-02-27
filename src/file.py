import io

from fun import *
from parse import *

# The file class
class File:
    def __init__(self, location):
        self.location = location

        self.raw = self.getRaw()
        self.name = self.getName()
        self.title = self.getTitle()
        self.template = self.getTemplate()
        self.tags = self.getTags()
        self.html = self.parse()

    # Parsing
    def parse(self):
        html = '<!--Made with Rocky Raccoon-->\n'
        for line in self.raw:
            html += transform(line)
        return html

    # Initializers
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

    def getTemplate(self):
        for line in self.raw:
            if getWord(line) == 'EXTENDS':
                return line[len('EXTENDS')+1:-1]
        return ''
    
    def getTitle(self):
        for line in self.raw:
            if getWord(line) == 'TITLE':
                return line[len('TITLE')+1:-1]
        return ''
    
    def getTags(self):
        for line in self.raw:
            if getWord(line) == 'TAGS':
                return line.split()[1:]
        return []

    # Redefines how the class behaves when asked to be printed
    def __repr__(self):
        repr = '\n'
        repr += 'NAME:' + self.name + '\n'
        repr += 'LOCATION:' + self.location + '\n'
        repr += 'TEMPLATE:' + self.template + '\n'
        repr += 'TAGS:'
        for tag in self.tags:
            repr += tag + ' '
        repr += '\n'
        repr += 'TITLE:' + self.title + '\n\n'

        return repr
