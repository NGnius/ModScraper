import scraper, os, sys
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums #array of all forum section links
def capsTDetector(): #If the first thread in a section is a new thread (0 replies) and the title is mostly caps, this will return a link to said thread
    capsTitles = []
    for i in range(0,len(forums)):
        scraper.page.ret(forums[i]) #load the page
        firstPostLink = scraper.page.findFirstPost() #find the first post
        scraper.page.ret(firstPostLink) #load first post page
        dates = scraper.page.findDates()
        if len(dates)==1:
            #find the title and compare it to the .lower() of it
    return capsTitles
def detectCapsT(link, mode="boolean"): 
