import wordSearcher
def FirstPost(rawpage): #finds the first post in a Robocraft forum section, through the use of (coding) magic
    lastUpdateLoc = wordSearcher.wordSearcher(" and was last updated by", rawpage, multipleLocs = False)[0]
    FirstPostLinkStart = lastUpdateLoc + wordSearcher.wordSearcher(" href=\"", rawpage[lastUpdateLoc:], output="lastChar")[2]
    '''Since the format is "last updated by [username link] [time elapsed and link to post] ago",
    and for some reason the user's profile is linked twice (don't ask me, I didn't write the website - I'm just cringing from it),
    the 3rd (2nd if you start from 0) href=" after "last updated by" is the link to the post'''
    FirstPostLinkEnd = FirstPostLinkStart + wordSearcher.wordSearcher("\"", rawpage[FirstPostLinkStart:], multipleLocs = False)[0] #find the closing " for the url
    return rawpage[FirstPostLinkStart:FirstPostLinkEnd]
