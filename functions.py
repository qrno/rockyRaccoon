import os

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
    def __init__(self, raw, location, name):
        self.raw = raw
        self.location = location
        self.name = name

        self.title = getTitle(self.raw)
        self.tags = getTags(self.raw)

    def __repr__(self):
        stringToRet = ''
        stringToRet += 'location: ' + self.location + '\n'
        stringToRet += 'name: ' + self.name + '\n'
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

def getWord(line, index):
    words = line.split()
    if len(words) - 1 < index:
        return ''
    return words[index]

def getFirstWord(line):
    return getWord(line, 0)

def getLocation(directory, filename):
    if directory[-1:] != '/':
        directory = directory+'/'
    return directory+filename

def cut(line, amountStart, amountEnd=0):
    if amountEnd == 0:
        return line[amountStart:]
    return line[amountStart:-amountEnd]

files = getFiles(inputDirectoryName, 'qmd')

def getList(fileList, tag='none'):
    if tag == 'none':
        return fileList

    desiredFiles = []
    for f in fileList:
        if tag in f.tags:
            desiredFiles.append(f)
    return desiredFiles

def formatList(elements, ordered=False):
    output = ''
    if ordered:
        output += '<ol>\n'
    else:
        output += '<ul>\n'

    for element in elements:
        output += '\t<li>'+element+'</li>\n'

    if ordered:
        output += '</ol>\n'
    else:
        output += '</ul>\n'
         
    return output


def formatLink(href, text):
    return '<a href="'+href+'">'+text+'</a>'
