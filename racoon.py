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
    hashCount = 0
    for char in line:
        if char == '#':
            hashCount += 1
        else:
            break
    if hashCount == 1:
        return (line[1: -1], 'h1')
    elif hashCount == 2:
        return (line[2: -1], 'h2')
    elif hashCount == 3:
        return (line[3: -1], 'h3')
    elif line[:6] == 'INSERT':
        return (line[7: -1], 'insert')
    else:
        return (line[:-1], 'p')

#The actual file by file treatment
for fileNow in inputFiles:

    templateFile = []
    out = []

    rawContent, name = fileNow

    outputFile = open('output/'+name+'.html', 'w')

    parsedContent = []
    for line in rawContent:
        parsedContent.append(parseLine(line))

    for line in parsedContent:
        content, kind = line

        if kind == 'h1':
            out.append('<h1>'+content+'</h1>\n')
        if kind == 'h2':
            out.append('<h2>'+content+'</h2>\n')
        if kind == 'h3':
            out.append('<h3>'+content+'</h3>\n')
        if kind == 'p':
            out.append('<p>'+content+'</p>\n')
        if kind == 'insert':
            templateLocation = 'input/templates/'+content+'.html'
            templateFile = open(templateLocation, 'r').readlines()

    for line in templateFile:
        outputFile.write(line)
        if line == '<!--CONTENT-->\n':
            for outLine in out:
                outputFile.write(outLine)
