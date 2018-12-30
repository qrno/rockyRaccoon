import io
from load import *
from parse import *

for file in files:

    html = ''

    for line in file.raw:
        html += prepare(line)

    outLocation = outputDir + file.name + '.html'
    outFile = io.open(outLocation, mode='w', encoding='utf-8')

    outFile.write(html)
