import scraper, os, time
dates = []
forumsToCheckFile = open(os.getcwd()+r"/Resources/ForumsToCheck.txt", "r")
forums = forumsToCheckFile.readlines()
forumsToCheckFile.close
def necroDetector()
    for i in range(0,len(forums)):
        necroPosts = []
        scraper.page.ret(forums[i])
        #the long thing here finds the link to the top post, as per the formating of the Robocraft forums
        #this involves finding the first link above the "Viewing [int] topics ...", which is the most recently updated post in the forum (forum section, technically)
        viewloc = scraper.wordSearcher.wordSearcher("Viewing",scraper.page.raw)[0]
        firstPostLinkLoc = viewloc - scraper.wordSearcher.wordSearcher("href="[::-1], scraper.page.raw[viewloc:0:-1])[0]
        firstPostLinkQuotes = scraper.wordSearcher.wordSearcher('"',scraper.page.raw[firstPostLinkLoc:viewloc])
        firstPostLink = scraper.page.raw[firstPostLinkQuotes[0]+firstPostLinkLoc+len('"'):firstPostLinkQuotes[1]+firstPostLinkLoc]
        print (firstPostLink)
        scraper.page.ret(firstPostLink)
        dateEnds = scraper.find(" at ")
        dates = []
        for i in range(len(dateEnds)):
            try:
                dates.append([time.strptime(scraper.page.text[dateEnds[i]-len("dd/mm/yyyy"):dateEnds[i]], "%d/%m/%Y"),dateEnds[i]])
            except:
                pass
        if dates[0][0][0] != dates[-1][0][0] and dates[-2][0][0] != dates[-1][0][0]: #check if the years match for first and last post as well as last and second last post
            print ("Boop: We have a necro from ", firstPostLink)
            necroPosts.append(firstPostLink)
    return necroPosts
