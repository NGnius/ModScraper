import scraper, os
def loadProfanity():
    '''()-> list of [str, int]
    load the Profanity.txt file'''
    file = scraper.fileIO.retrieveFile(os.getcwd()+r"/Resources/Profanity.txt")
    profanity = [] #in format [word, weight] - word is the profanity word, while weight is the value that is added everytime that word is encountered
    word = ""
    for i in file: #parse the file to get swear words and their weight
        if (i == " " or i =="\n") and word!="":
            try:
                profanity[len(profanity)-1][1]=int(word) #if it's a number, overwrite the weight of the last word
            except:
                profanity.append([word.lower(), 1])
            word = ""
        elif i!=" " and i!="\n":
            word += i
    if word !="": #make sure the last item doesn't get forgotten
        try:
            profanity[len(profanity)-1][1]=int(word)
        except:
            profanity.append([word.lower(), 1])
    return profanity
