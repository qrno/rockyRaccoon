import io
from load import *
from parse import *
from render import *

files = getFiles(inputDir, fileExtension)
for file in files:
    outLocation = outputDir + file.name + '.html'
    templateName = file.template + '.html'

    outFile = io.open(outLocation, mode='w', encoding='utf-8')

    outFile.write(render(templateDir+templateName,file))

