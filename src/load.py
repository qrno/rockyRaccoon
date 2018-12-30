import os

from fun import *
from file import File

inputDir = '../input/'
outputDir = '../output/'
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
    return files

files = getFiles(inputDir, fileExtension)
print(files)
