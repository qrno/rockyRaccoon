# Gets the nth word
# If no n is provided, n=0
def getWord(line, n=0):
    words = line.split() 

    # In case there is no such word
    if len(words) <= n:
        return ''

    return words[n]

# Gets file extension
def getExtension(filename):
    # Divides filename in parts (ex: lol.py -> ['lol', 'py']
    parts = filename.split('.')

    # Gets last part 'py'
    last = parts[-1:][0]

    return last
