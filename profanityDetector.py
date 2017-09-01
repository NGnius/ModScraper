'''Detect profanity in the last post'''
import Profanity
profanityList = Profanity.loadProfanity() #load the list of profanity and weights

def isProfanity(post, threshold): #returns True if the post is above the swear threshold, False if not
    output = False
    postDates = post.findDates()
    swearCount = 0
    if len(postDates) > 0: #make sure the page isn't glitched and has at least one post (this prevents a crash)
        for j in profanityList: #search for each swear word in the last post of the thread, and then up the swear count accordingly
            instances = len(post.search(j[0], post.text[postDates[-1][1]:]))
            swearCount += instances*j[1] #increase the swearCount by the number of times the word was used times the weight of that swear word
    if swearCount > threshold: #if the poster has sworn too much
        output = True
    return output
