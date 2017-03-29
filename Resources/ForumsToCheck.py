import scraper, os, time
def loadFile():
    global forums
    forumsToCheckFile = open(os.getcwd()+r"/Resources/ForumsToCheck.txt", "r")
    forums = forumsToCheckFile.readlines()
    forumsToCheckFile.close
