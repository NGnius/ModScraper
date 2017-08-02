import scraper, os, sys
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, config
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums #array of all forum section links
arbitraryCapsCountAntiThreshold = config.retrieveConfig("CapsTitleThreshold")

def isCaps(string, threshold = 1): #find capitalised parts of a string
    #returns True if the number of capitalised letters is greater than/equal to the threshold
    output = False
    capsCount = 0
    for char in string:
        if char.lower() != char:
            capsCount +=1
        if capsCount >= threshold:
            output = True
            break
    return output

def hasCapsT(postLink, mode="boolean"): #detect if the title of a post is all caps
    output = False
    scraper.page.ret(postLink)
    title = scraper.page.findTopicTitle()
    print(title)
    if arbitraryCapsCountAntiThreshold >= 0: #if threshold number is less than 0, add the amount to the string length
        isCapsResult = isCaps(title, threshold = arbitraryCapsCountAntiThreshold)
    else:
        isCapsResult = isCaps(title, threshold = len(title)+arbitraryCapsCountAntiThreshold)

    if isCapsResult:
        if mode == "boolean":
            output = True
        if mode == "link":
            output = postLink
        if mode == "title":
            output = title
    return output

def capsTDetector(): #If the first thread in a section is a new thread (0 replies) and the title is mostly caps, this will return a link to said thread
    capsTitles = []
    for i in range(0,len(forums)):
        scraper.page.ret(forums[i]) #load the page
        firstPostLink = scraper.page.findFirstPost() #find the first post
        if hasCapsT(firstPostLink):
            capsTitles.append(firstPostLink)
    return capsTitles

def detectCapsT(link, mode="boolean"): #detect if most recent thread has lots of Caps in the title
    #boolean mode returns True if lots of caps are detected, False if not
    #link mode returns the link to the post if lots of caps are detected, False if not
    #title mode returns the topic's title to the post if ltos of caps are detected, False if not
    scraper.page.ret(link)
    firstPostLink = scraper.page.findFirstPost()
    return hasCapsT(firstPostLink, mode=mode)

def detectAllCapsT(link, mode="list"): #WIP, untested and probably doesn't work, link must be a URL for a Robocraft forum section
    #list mode returns a list of all posts which have lots of caps in their titles
    #boolean mode returns True as soon as a post if found with lots of caps in it's title
    #count mode returns the number of threads with lots of caps in their titles
    output = []
    scraper.page.ret(link)
    posts = scraper.page.findAllPosts()
    for post in posts:
        if hasCapsT(post):
            if mode == "list":
                output.append(post)
            elif mode == "boolean":
                output = True
                break
            elif mode == "count":
                if output == []:
                    output = 1
                else:
                    output += 1
    return output
