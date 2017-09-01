'''This actually runs everything'''

import sys, os, time
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, scraper, config
import necroDetector, profanityDetector, capsDetector
page = scraper.pageClass()
post = scraper.pageClass()

def main(): #main function, goes through the all the stuff
    global page, post
    startTime = time.time() #for science!
    for f in ForumsToCheck.forums: #check each forum sequentially
        print("Scraping", f) #debug
        page.ret(f)
        check = "all"
        if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
            pagePosts = page.findAllPosts()
            for p in pagePosts: #go through all the posts in section f and check them according to the config
                post.ret(p)
                if config.retrieveConfig("NecroDetection")==check:
                    if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
                        print(p, " has been bumped from the dead.")
                if config.retrieveConfig("ProfanityDetection")==check:
                    if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
                        print(p, " has been sworn in a lot.")
                if config.retrieveConfig("CapsTitleDetection")==check:
                    if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
                        print(p," has a lot of caps in the title.")
        check = "first"
        if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
            p = page.findFirstPost() #check the first post in section f according to the config
            post.ret(p)
            if config.retrieveConfig("NecroDetection")==check:
                if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
                    print(p, " has been bumped from the dead.")
            if config.retrieveConfig("ProfanityDetection")==check:
                if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
                    print(p, " has been sworn in a lot.")
            if config.retrieveConfig("CapsTitleDetection")==check:
                if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
                    print(p," has a lot of caps in the title.")

    elapsedTime = time.time()-startTime #for science!
    print ("Elapsed Time (s): ", elapsedTime) #for science!
    if elapsedTime < config.retrieveConfig("Period"): #if the period specified in config hasn't elapsed completely
        print("Sleeping") #debug
        time.sleep(config.retrieveConfig("Period")-elapsedTime) #sleep until the period time has elapsed
