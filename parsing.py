from functions import *

'''On functions.py
getTitle(raw)
getTags(raw)
class File
getFileExtension(filename)
cutExtension(filename)
getFiles(directory, fileExtension)
getWord(line, index)
getFirstWord(line)
getLocation(directory, filename)
cut(line, amountStart, amountEnd=0)
getList(fileList, tag='none')
formatLink(href, text)
formatList(elements, ordered=False)
'''
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
        formattedFileList.append(formatLink(f.name+'.html', f.title))
    return formatList(formattedFileList)

def getPackets(raw):
    packets = []

    pOpen = False
    packet = ('','')
    for line in raw:
        pass
