import scraper, os, time, sys
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums
def necroDetector(): #return each thread that has a last post with a different year than the second last and first post in the same thread, if it is the most
    #recently updated thread in the given section, as per the forum sections stored in the ForumsToCheck.txt file
    for i in range(0,len(forums)):
        necroPosts = []
        scraper.page.ret(forums[i])
        #the long thing here finds the link to the top post, as per the formating of the Robocraft forums
        #this involves finding the first link above the "Viewing [int] topics ...", which is the most recently updated post in the forum (forum section, technically)
        viewloc = scraper.wordSearcher.wordSearcher("Viewing",scraper.page.raw)[0]
        firstPostLinkLoc = viewloc - scraper.wordSearcher.wordSearcher("href="[::-1], scraper.page.raw[viewloc:0:-1])[0]
        firstPostLinkQuotes = scraper.wordSearcher.wordSearcher('"',scraper.page.raw[firstPostLinkLoc:viewloc])
        firstPostLink = scraper.page.raw[firstPostLinkQuotes[0]+firstPostLinkLoc+len('"'):firstPostLinkQuotes[1]+firstPostLinkLoc]
        #find all of the dates of the posts on the page (if the thread has more than one page, this will only check the last page, which shouldn't matter)
        #of course, if the new post that necroed the post creates a new page, this will completely miss it (Reminder: Fix that)
        scraper.page.ret(firstPostLink)
        dateEnds = scraper.find(" at ")
        dates = []
        for i in range(len(dateEnds)):
            try:
                dates.append([time.strptime(scraper.page.text[dateEnds[i]-len("dd/mm/yyyy"):dateEnds[i]], "%d/%m/%Y"),dateEnds[i]])
            except:
                pass
        #check if the years match for first and last post as well as last and second last post
        if len(dates)>1:
            if dates[0][0][0] != dates[-1][0][0] and dates[-2][0][0] != dates[-1][0][0]:
                print ("Boop: We have a necro from ", firstPostLink) #Don't judge my booping
                necroPosts.append(firstPostLink)
    return necroPosts

def detectNecro(link, mode = "boolean"): #detect if most recent thread in link has been bumped from a different year
        #boolean mode returns if the first post has been necroed (True if it has been, False if not)
        #link mode returns the link of the necroed thread if the first post has been necroed, boolean False if not
        output = False
        scraper.page.ret(link)
        #the long thing here finds the link to the most recently updated thread, as per the formating of the Robocraft forums
        #this involves finding the first link above the "Viewing [int] topics ...", which is the most recently updated post in the forum (forum section, technically)
        viewloc = scraper.wordSearcher.wordSearcher("Viewing",scraper.page.raw)[0]
        firstPostLinkLoc = viewloc - scraper.wordSearcher.wordSearcher("href="[::-1], scraper.page.raw[viewloc:0:-1])[0]
        firstPostLinkQuotes = scraper.wordSearcher.wordSearcher('"',scraper.page.raw[firstPostLinkLoc:viewloc])
        firstPostLink = scraper.page.raw[firstPostLinkQuotes[0]+firstPostLinkLoc+len('"'):firstPostLinkQuotes[1]+firstPostLinkLoc]
        #find all of the dates of the posts on the page (if the thread has more than one page, this will only check the last page, which shouldn't matter)
        scraper.page.ret(firstPostLink)
        dateEnds = scraper.find(" at ")
        dates = []
        for i in range(len(dateEnds)):
            try:
                dates.append([time.strptime(scraper.page.text[dateEnds[i]-len("dd/mm/yyyy"):dateEnds[i]], "%d/%m/%Y"),dateEnds[i]])
            except:
                pass
        #check if the years match for first and last post as well as last and second last post and set output appropriately
        if len(dates)>1: #to prevent the module from crashing if the thread has only one post in it (it's a new thread and only has the OP's 1st post)
            if dates[0][0][0] != dates[-1][0][0] and dates[-2][0][0] != dates[-1][0][0]:
                print ("Boop: We have a necro from ", firstPostLink) #don't ask; printing weird things is more fun
                if mode == "boolean":
                    output = True
                if mode == "link":
                    output == firstPostLink
        return output
