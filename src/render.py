import io
from load import *

def render(templateLocation, file):
    templateIO = io.open(templateLocation, mode='r', encoding='utf-8')
    template = templateIO.readlines()

    toRet = ''
    for line in template:
        line = line.replace('[[ TITLE ]]', file.title)
        line = line.replace('[[ CONTENT ]]', file.html)
        line = line.replace('[[ TEMPLATE ]]', templateDir)
        toRet += line

    return toRet
