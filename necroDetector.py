import scraper, os, time, sys, config
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck
ForumsToCheck.loadFile()
forums = ForumsToCheck.forums #array of all forum section links

def timeDelta(a,b): #subtracts the time, in seconds, between struct_time a and b
    return abs( (((b.tm_year*365)+b.tm_yday)*24*60*60) - (((a.tm_year*365)+a.tm_yday)*24*60*60) )

def isNecro(postLink, mode = "boolean"): #detect if post postLink has been necroed
    #boolean mode returns True if the post has been necroed, False if not
    #link mode returns postLink if the post has been necroed, False if not
    output = False
    scraper.page.ret(postLink) #load page
    dates = scraper.page.findDates() #find all the post and reply dates in the post
    #check if the years match for first and last post as well as last and second last post and set output appropriately
    if len(dates)>1: #to prevent the module from crashing if the thread has only one post in it (it's a new thread and only has the OP's 1st post)
        if timeDelta(dates[0][0], dates[-1][0])>config.retrieveConfig("NecroTimeDelta") and timeDelta(dates[-2][0], dates[-1][0])>config.retrieveConfig("NecroTimeDelta"):
            print ("Boop: We have a necro from ", postLink) #don't ask; printing weird things is more fun
            if mode == "boolean":
                output = True
            if mode == "link":
                output == postLink
    return output

def necroDetector(): #return links to each first thread in each forum section with a last post that is a different year than the second last and first post in the same thread
    necroPosts = []
    for i in range(0,len(forums)):
        scraper.page.ret(forums[i]) #load the page
        firstPostLink = scraper.page.findFirstPost() #find the first post
        if isNecro(firstPostLink):
            necroPosts.append(firstPostLink)
    return necroPosts

def detectNecro(link, mode = "boolean"): #detect if most recent thread in forum section has been bumped from a different year, link must be a URL for a Robocraft forum section
    #boolean mode returns if the first post has been necroed (True if it has been, False if not)
    #link mode returns the link of the necroed thread if the first post has been necroed, boolean False if not
    scraper.page.ret(link) #load page
    firstPostLink = scraper.page.findFirstPost() #find the first post
    return isNecro(firstPostLink, mode=mode)

def detectAllNecros(link, mode = "list"): #WIP, untested and probably doesn't work, link must be a URL for a Robocraft forum section
    #list mode returns a list of all threads which are necroed in the forum section
    #boolean mode returns True as soon as it encounters a necroed thread in the forum section
    #count mode returns the number of necroed threads in the forum section
    output = []
    scraper.page.ret(link)
    posts = scraper.page.findAllPosts() #find all posts in the forum section
    for post in posts:
        if isNecro(post):
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
