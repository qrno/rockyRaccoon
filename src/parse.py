from fun import *

templates = {
    'h1'    : '<h1>\E0</h1>',
    'h2'    : '<h2>\E0</h2>',
    'p'     : '<p>\E0</p>',
    'com'   : '<!--\E0-->',
    'nothing' : ''
}

reservedWords = ['TITLE', 'TAGS', 'EXTENDS']

def parse(line):
    first = getWord(line)
    rest = line[len(first)+1:]

    if first == '#':
        return [rest], 'h1'
    if first == '##':
        return [rest], 'h2'
    if first == '@':
        return [rest], 'com'
    if first in reservedWords:
        return [], 'nothing'

    return [line], 'p'

def transform(line):
    elements, type = parse(line)

    parsed = templates[type]
    for i in range(len(elements)):
        parsed = parsed.replace('\E'+str(i), elements[i])
    return parsed
