import scraper, os
forumsToCheckFile = open(os.getcwd()+r"/Resources/ForumsToCheck.txt", "r")
forums = forumsToCheckFile.readlines()
forumsToCheckFile.close
print (forums)

for i in range(0,len(forums)):
    scraper.page.ret(forums[i])
    #the long thing here finds the link to the top post, as per the formating of the Robocraft forums
    #this involves finding the first link above the "Viewing [int] topics ...", which is the most recently updated post in the forum (forum section, technically)
    viewloc = scraper.wordSearcher.wordSearcher("Viewing",scraper.page.raw)[0]
    firstPostLinkLoc = viewloc - scraper.wordSearcher.wordSearcher("href="[::-1], scraper.page.raw[viewloc:0:-1])[0]
    firstPostLinkQuotes = scraper.wordSearcher.wordSearcher('"',scraper.page.raw[firstPostLinkLoc:viewloc])
    firstPostLink = scraper.page.raw[firstPostLinkQuotes[0]+firstPostLinkLoc+len('"'):firstPostLinkQuotes[1]+firstPostLinkLoc]
    print (firstPostLink)
