from parsing import *

for fileNow in files:
    outString = ''
    pOpen = False
    for line in fileNow.raw:
        outString += prepareLine(line, pOpen)
        first = getFirstWord(line)
    templateLocation = inputDirectoryName + '/templates/'+fileNow.template+'.html'
    templateContent = io.open(templateLocation, mode='r', encoding='utf-8').readlines()

    newString = ''
    for line in templateContent:
        line = line.replace('<!--TITLE-->', fileNow.title)
        line = line.replace('<!--CONTENT-->', outString)
        newString += line

    print(fileNow)

    outputLocation = outputDirectoryName+'/'+fileNow.name+'.html'
    outputFile = io.open(outputLocation, mode='w', encoding='utf-8')
    outputFile.write(newString)
