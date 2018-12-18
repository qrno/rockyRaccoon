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
    elif first == '=':
        return (line,'p')
    elif first == 'IMAGE':
        return (line[len('IMAGE'):-1], 'image')
    elif first in reservedWords:
        return (line, 'comment')
    else:
        return (line, 'none')

def convertLine(content, kind, pOpen):
    if kind == 'h1':
        return '<h1>'+ content +'</h1>'
    if kind == 'h2':
        return '<h2>'+ content +'</h2>'
    if kind == 'h3':
        return '<h3>'+ content +'</h3>'
    if kind == 'p':
        if (not pOpen):
            return '<p>'
        else:
            return '</p>'
    if kind == 'comment':
        return '<!--'+content+'-->'
    if kind == 'image':
        return '<img src="'+content+'">'
    else:
        return content

def prepareLine(line, pOpen):
    if getFirstWord(line) == 'LIST':
        listName = cut(line, len('LIST')+1, 1)
        listElements = getList(files, listName)
        listHTML = formatList(listElements)
        return listHTML
    content, kind = parseLine(line)
    convertedLine = convertLine(content, kind, pOpen)
    return convertedLine + '\n'
