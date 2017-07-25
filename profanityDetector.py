import scraper, os
import ForumsToCheck, Profanity
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums #array of all forum section links
arbitrarySwearCountThreshold = 20

def countProfanity (postLink, mode="count"): #count swear words in post postLink
    #count mode returns the swear count of the post
    #boolean mode returns True if the post is above the swear threshold, False if not
    output = False
    scraper.page.ret(postLink)
    postDates = scraper.page.findDates()
    swearCount = 0
    for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
        instances = len(scraper.wordSearcher.wordSearcher(j[0], scraper.page.text[postDates[-1][1]:]))
        swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
    if swearCount > arbitrarySwearCountThreshold: #arbitrary number that says that the poster has sworn too much when exceeded
        output = True
    if mode == "count":
        return swearCount
    elif mode == "boolean":
        return output

def profanityDetector(): #detects all profanity in the first posts of the designated forum sections, returns an array of threads with too much swearing
    profanityOverloads = []
    for i in forums:
        scraper.page.ret(i) #load page
        firstPost = scraper.page.findFirstPost() #find the first post
        if countProfanity(firstPost) > arbitrarySwearCountThreshold:
            print("Boop: We have a swear overload in ", i)
            profanityOverloads.append(i)
    return profanityOverloads

def detectProfanity(link, mode="boolean"): #detect if most recent thread in forum section is above the swear threshold, link must be a URL for a Robocraft forum section
    #boolean mode returns True if the first post is above the swear threshold, False if not
    #link mode returns the first post's link if said post is above the threshold, False if not
    #count mode returns the swearcount of the thread if it is above the threshold, False if not
    output = False
    scraper.page.ret(link) #load page
    firstPost = scraper.page.findFirstPost() #find the first post in the page
    swearCount = countProfanity(firstPost) #get the swear count for that first post
    if swearCount > arbitrarySwearCountThreshold: #generate the output
        if mode=="boolean":
            output=True
        elif mode=="link":
            output=firstPostLink
        elif mode=="count":
            output=swearCount
    return output

def detectAllProfanity(link, mode="list"):#WIP, untested and probably doesn't work, link must be a URL for a Robocraft forum section
    #list mode returns a list of all threads which are above the swear threshold in the forum section
    #boolean mode returns True as soon as it encounters a thread above the threshold in the forum section
    #count mode returns the number of threads above the swear threshold in the forum section
    output = []
    scraper.page.ret(link)
    posts = scraper.page.findAllPosts()
    for post in posts:
        if countProfanity(post) > arbitrarySwearCountThreshold:
            if mode=="list":
                output=post
            elif mode=="boolean":
                output = True
                break
            elif mode == "count":
                if output == []:
                    output = 1
                else:
                    output += 1
    return output

profanityList = Profanity.loadProfanity()
