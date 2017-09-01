import scraper, os
import ForumsToCheck, Profanity, config
ForumsToCheck.loadFile()
profanityList = Profanity.loadProfanity()
forums = ForumsToCheck.forums #array of all forum section links
arbitrarySwearCountThreshold = config.retrieveConfig("SwearThreshold")

def countProfanity (post, threshold, mode="count"): #count swear words in post postLink
    #count mode returns the swear count of the post
    #boolean mode returns True if the post is above the swear threshold, False if not
    output = False
    postDates = post.findDates()
    swearCount = 0
    for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
        instances = len(scraper.wordSearcher.wordSearcher(j[0], post.text[postDates[-1][1]:]))
        swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
    if swearCount > threshold: #arbitrary number that says that the poster has sworn too much when exceeded
        output = True
    if mode == "count":
        return swearCount
    elif mode == "boolean":
        return output

def isProfanity(post, threshold):
    #count mode returns the swear count of the post
    #boolean mode returns True if the post is above the swear threshold, False if not
    output = False
    postDates = post.findDates()
    swearCount = 0
    if len(postDates) > 0:
        for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
            instances = len(scraper.wordSearcher.wordSearcher(j[0], post.text[postDates[-1][1]:]))
            swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
    if swearCount > threshold: #arbitrary number that says that the poster has sworn too much when exceeded
        output = True
    return output
