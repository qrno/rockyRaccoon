import os

from fun import *
from file import *

inputDir = '../input/'
outputDir = '../output/'
templateDir = inputDir + 'templates/'
fileExtension = 'qmd'

def getFiles(dir, ext):
    # All filenames from dir
    filenames = os.listdir(dir)

    files = []
    for filename in filenames:
        if getExtension(filename) == ext:

            location = dir + filename
            file = File(location)

            files.append(file)
    print("Loaded Files: ")
    print(files)
    return files
