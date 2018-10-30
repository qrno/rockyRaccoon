#Navigating through UNIX filesystem'
import os
import pprint as pp

#Gets file names in input/
inputDir = os.listdir('input')
qmdFiles = []

for f in inputDir:
    if f[-4:] == '.qmd':
        qmdFiles.append(f[:-4])

#Gets and opens all files/
inputFiles = []
for fileName in qmdFiles:
    fileLocation = 'input/'+fileName+'.qmd'
    inputFiles.append((open(fileLocation, 'r').readlines(), fileName))

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
    elif first == 'EXTENDS':
        return (line.split()[1], 'extends')
    elif first == '@':
        return (line[1: -1], 'comment')
    elif first == '!':
        if line.split()[1] == 'LIST':
            return ('list', 'command')
    elif first == '=':
        return (line[1:-1], 'pInit')
    else:
        return (line[:-1], 'pCont')

#The actual file by file treatment
for fileNow in inputFiles:
    templateFile = []
    out = []

    rawContent, name = fileNow

    outputFile = open('output/'+name+'.html', 'w')

    parsedContent = []
    for line in rawContent:
        parsedContent.append(parseLine(line))

    pOpen = False

    for line in parsedContent:
        content, kind = line

        if kind == 'h1':
            out.append('<h1>'+content+'</h1>\n')
        if kind == 'h2':
            out.append('<h2>'+content+'</h2>\n')
        if kind == 'h3':
            out.append('<h3>'+content+'</h3>\n')
        if kind == 'pInit':
            if not pOpen:
                out.append('<p>'+content+'\n')
            else:
                out.append('</p>\n')
            pOpen = not pOpen
        if kind == 'pCont':
            out.append(content+'\n')
        if kind == 'extends':
            templateLocation = 'input/templates/'+content+'.html'
            templateFile = open(templateLocation, 'r').readlines()
        if kind == 'comment':
            out.append('<!--'+content+'-->')
        if kind == 'command' and content == 'list':
            out.append('<ul>')
            for f in inputFiles:
                name = f[1]
                if name != 'home':
                    out.append('<li><a href="'+name+'.html">'+name+'</a>\n')
            out.append('</ul')

    for line in templateFile:
        if '<!--CONTENT-->' in line:
            for outLine in out:
                outputFile.write(outLine)
            continue
        outputFile.write(line)
