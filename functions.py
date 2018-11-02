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
    first = getFirstWord(line)
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
    if kind == 'link':
        return '<a href='+content+'>'+content+'</a>'
    else:
        return '<!--'+content+'-->'

def getList(fileList, tag='none'):
    if tag == 'none':
        return fileList

    desiredFiles = []
    for f in fileList:
        if tag in f.tags:
            desiredFiles.append(f)
    return desiredFiles

def formatLink(href, inside):
    return '<a href="'+href+'">'+inside+'</a>'

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
    
def getHTML(f):
    return f.name+'.html'

def prepareLine(line, files):
    if getFirstWord(line) == 'LIST':
        return prepareList(files, line.split()[1])

    content, kind = parseLine(line)
    convertedLine = convertLine(content, kind)
    return convertedLine + '\n'

def prepareList(files, tag):
    fileList = getList(files, tag)
    formattedFileList = []
    for f in fileList:
        formattedFileList.append(formatLink(getHTML(f), f.title))
    return formatList(formattedFileList)
    
for fileNow in files:
    outLocation = getLocation(outputDirectoryName, fileNow.name) + '.html'
    outString = ''

    for line in fileNow.raw:
        outString += prepareLine(line, files)

    outFile = open(outLocation, 'w')
    outFile.write(outString)
