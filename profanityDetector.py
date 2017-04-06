import scraper, os
import ForumsToCheck
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums
def loadProfanity():
    file = scraper.fileIO.retrieveFile(os.getcwd()+r"/Resources/Profanity.txt")
    profanity = [] #in format [word, weight] - word is the profanity word, while
    word = ""
    for i in file:
        if (i == " " or i =="\n") and word!="":
            try:
                profanity[len(profanity)-1][1]=int(word) #if it's a number, overwrite the weight of the last word
            except:
                profanity.append([word.lower(), 1])
            word = ""
        elif i!=" " and i!="\n":
            word += i
    try: #make sure the last item doesn't get forgotten
        profanity[len(profanity)-1][1]=int(word) 
    except:
        profanity.append([word.lower(), 1])
    return profanity

def profanityDetector(): #detects all profanity in the designated forum sections
    for i in forums:
        scraper.page.ret(i)
        firstPost = scraper.page.findFirstPost()
        scraper.page.ret(firstPost)
        postDates = scraper.page.findDates()
        swearCount = 0
        for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
            instances = len(scraper.wordSearcher.wordSearcher(j[0], scraper.page.text[postDates[-1][1]:]))
            swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
        if swearCount > 20: #arbitrary number that says that the poster has sworn too much when exceeded
            print("Boop: We have a swear overload in ", i)

def detectProfanity(link, mode="boolean"):
    output = False
    scraper.page.ret(link)
    firstPost = scraper.page.findFirstPost()
    scraper.page.ret(firstPost)
    postDates = scraper.page.findDates()
    swearCount = 0
    for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
        instances = len(scraper.wordSearcher.wordSearcher(j[0], scraper.page.text[postDates[-1][1]:]))
        swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
    if swearCount > 20: #arbitrary number that says that the poster has sworn too much when exceeded
        if mode.lower()== "boolean":
            output = True
        if mode == "link":
            output = firstPost
    return output
            
            

profanityList = loadProfanity()


    
