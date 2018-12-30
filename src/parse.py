from fun import *

templates = {
    'h1'    : '<h1>\E0</h1>',
    'h2'    : '<h2>\E0</h2>',
    'p'     : '<p>\E0</p>',
    'com'   : '<!--\E0-->'
}

def parse(line):
    first = getWord(line)
    rest = line[len(first)+1:]

    if first == '#':
        return [rest], 'h1'
    if first == '##':
        return [rest], 'h2'
    if first == '@':
        return [rest], 'com'
    
    return [line], 'p'

def transform(elements, type):
    templ = templates[type]
    for i in range(len(elements)):
        templ = templ.replace('\E'+str(i), elements[i])
    return templ

def prepare(line):
    elements, type = parse(line)
    return transform(elements, type)
