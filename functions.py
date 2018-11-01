import os
import pprint as pp

inputDirectoryName = 'input'
outputDirectoryName = 'output'
fileExtensionName = 'qmd'
reservedWords = ['TITLE', 'TAGS', 'EXTENDS', 'IMAGE', 'LIST']

def getTitle(raw):
    for line in raw:
        if getFirstWord(line) == 'TITLE':
            return cut(line, len('TITLE'), 1)
    return ''

def getTags(raw):
    tags = []
    for line in raw:
        if getFirstWord(line) == 'TAGS':
            return line.split()[1:]
    return ''

class File:
    def __init__(self, raw, location, filename):
        self.raw = raw
        self.location = location
        self.filename = filename

        self.title = getTitle(self.raw)
        self.tags = getTags(self.raw)

    def __repr__(self):
        stringToRet = ''
        stringToRet += 'location: ' + self.location + '\n'
        stringToRet += 'filename: ' + self.filename + '\n'
        stringToRet += 'tags: '
        for tag in self.tags:
            stringToRet += tag + ' '
        stringToRet += '\n'
        stringToRet += 'title: ' + self.title + '\n'
        return stringToRet

def getFileExtension(filename):
    for idx, char in enumerate(filename):
        if char == '.':
            return filename[idx+1:]
    return ''

def cutExtension(filename):
    extensionSize = len(getFileExtension(filename)) + 1
    return filename[:-extensionSize]


def getFiles(directory, fileExtension):
    files = os.listdir(directory)
    fileList = []
    for filename in files:
        if getFileExtension(filename) == fileExtension:
            location = getLocation(directory, filename)
            content = open(location, 'r').readlines()
            f = File(content, location, cutExtension(filename))
            fileList.append(f)
    return fileList

def getFirstWord(line):
    words = line.split()
    if words != []:
        return words[0]
    else:
        return ''

def getLocation(directory, filename):
    if directory[-1:] != '/':
        directory = directory+'/'
    return directory+filename

def cut(line, amountStart, amountEnd=0):
    if amountEnd == 0:
        return line[amountStart:]
    return line[amountStart:-amountEnd]

files = getFiles(inputDirectoryName, 'qmd')

#Parsing
def parseLine(line):
    first = ''
    if line != '\n':
        first = line.split()[0]
    if first == '#':
        return (line[1: -1], 'h1')
    elif first == '##':
        return (line[2: -1], 'h2')
    elif first == '###':
        return (line[3: -1], 'h3')
    elif first == '@':
        return (line[1: -1], 'comment')
    elif first in reservedWords:
        return ('', 'comment')
    else:
        return (line[:-1], 'p')

def convertLine(content, kind):
    if kind == 'h1':
        return '<h1>'+ content +'</h1>'
    if kind == 'h2':
        return '<h2>'+ content +'</h2>'
    if kind == 'h3':
        return '<h3>'+ content +'</h3>'
    if kind == 'p':
        return '<p>'+ content + '</p>'
    else:
        return '<!--'+content+'-->'

#The actual file by file treatment
for fileNow in files:
    outLocation = getLocation(outputDirectoryName, fileNow.filename) + '.html'
    out = open(outLocation, 'w')
    for line in fileNow.raw:
        content, kind = parseLine(line)
        convertedLine = convertLine(content, kind)
        print(convertedLine)
        out.write(convertedLine+'\n')
