import scraper, os
import ForumsToCheck, Profanity
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums #array of all forum section links

def profanityDetector(): #detects all profanity in the designated forum sections, returns an array of threads with too much swearing
    profanityOverloads = []
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
            profanityOverloads.append(i)
    return profanityOverloads

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



profanityList = Profanity.loadProfanity()
