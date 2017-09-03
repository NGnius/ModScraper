'''This actually runs everything'''

import sys, os, time
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, scraper, config, log_it
import necroDetector, profanityDetector, capsDetector
page = scraper.pageClass()
post = scraper.pageClass()
log_it.logg("Startup successful", genus=["log", "debug"])

def main(): #main function, goes through the all the stuff
    global page, post
    startTime = time.time() #for science!
    log_it.logg("Starting scraping round", genus=["debug"])
    for f in ForumsToCheck.forums: #check each forum sequentially
        log_it.logg("Scraping section "+ f, genus=["debug"])
        page.ret(f)
        check = "all"
        if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
            pagePosts = page.findAllPosts()
            for p in pagePosts: #go through all the posts in section f and check them according to the config
                post.ret(p)
                log_it.logg("Scraping " + p, genus=["debug","verbose"])
                if config.retrieveConfig("NecroDetection")==check:
                    if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
                        log_it.logg(p + " has been bumped from the dead.", genus=["output"])
                if config.retrieveConfig("ProfanityDetection")==check:
                    if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
                        log_it.logg(p + " has been sworn in a lot.", genus=["output"])
                if config.retrieveConfig("CapsTitleDetection")==check:
                    if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
                        log_it.logg(p + " has a lot of caps in the title.", genus=["output"])
        check = "first"
        if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
            p = page.findFirstPost() #check the first post in section f according to the config
            log_it.logg("Scraping " + p)
            post.ret(p)
            if config.retrieveConfig("NecroDetection")==check:
                if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
                    log_it.logg(p + " has been bumped from the dead.", genus=["output"])
            if config.retrieveConfig("ProfanityDetection")==check:
                if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
                    log_it.logg(p + " has been sworn in a lot.", genus=["output"])
            if config.retrieveConfig("CapsTitleDetection")==check:
                if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
                    log_it.logg(p + " has a lot of caps in the title.", genus=["output"])

    elapsedTime = time.time()-startTime #for science!
    log_it.logg ("Time elapsed in latest scrape: " + str(elapsedTime), genus=["debug", "benchmarking"])
    if elapsedTime < config.retrieveConfig("Period"): #if the period specified in config hasn't elapsed completely
        log_it.logg("Sleeping", genus=["debug"]) #debug
        time.sleep(config.retrieveConfig("Period")-elapsedTime) #sleep until the period time has elapsed
