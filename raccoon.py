from parsing import *

for fileNow in files:
    outLocation = getLocation(outputDirectoryName, fileNow.name) + '.html'
    outString = ''

    for line in fileNow.raw:
        outString += prepareLine(line, files)

    outFile = open(outLocation, 'w')
    outFile.write(outString)
