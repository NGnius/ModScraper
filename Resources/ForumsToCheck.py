import scraper, os, time
def loadFile(): #loads each line of the file (which is a url) as an item in the array
    global forums #this way you can do ForumsToCheck.forums to get the forums array from the module
    forumsToCheckFile = open(os.getcwd()+r"/Resources/ForumsToCheck.txt", "r")
    forums = forumsToCheckFile.readlines()#put each line as a seperate item in an array
    forumsToCheckFile.close
    for i in range(len(forums)): #remove /n at the end of each line
        if forums[i][-1]=="\n":
            forums[i]=forums[i][:-1]
                
loadFile()
