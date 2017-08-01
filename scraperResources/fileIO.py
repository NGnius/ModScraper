"""This is for opening and closing files with a few other features tucked in
for fun"""
def addToFile(filename, information, overwrite=False):
    if overwrite:
        file = open(filename, "w")
        file.write(information)
        file.close()
    else:
        try:
            file = open(filename, "r")
            filetowrite =file.read()+information
            file.close()
            file = open(filename, "w")
            file.write(filetowrite)
            file.close()
        except:
            file = open(filename, "w")
            file.write(information)
            file.close()
    return True

def retrieveFile(filename, binary=False): #retrieve file at location filename, return file contents
    if binary:
        file = open(filename, "rb")
    else:
        file = open(filename, "r")
    fileInfo = file.read()
    file.close() #always close your files, kids!
    return fileInfo

def retrieveFileLines(filename, binary=False):
    if binary:
        file = open(filename, "rb")
    else:
        file = open(filename, "r")
    fileInfo = file.readlines()
    file.close() #always close your files, kids!
    return fileInfo

def writeFile(filename, information, binary=False, returnFile=False): #write information to file a location filename
    if binary:
        file = open(filename, "wb")
    else:
        file = open(filename, "w")
    file.write(information)
    file.close()
    if returnFile:
        if binary:
            file = open(filename, "rb")
            fileInfo=file.read()
        else:
            file = open(filename, "r")
            fileInfo=file.read()
        file.close()
        return fileInfo
    else:
        return True
