'''This actually runs everything'''

import sys, os, time
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, scraper, config, log_it
import necroDetector, profanityDetector, capsDetector
from multiprocessing import Process

def init(queue):
    global q
    q = queue

def main():
    '''() -> None
    main function, goes through the all the stuff'''
    startTime = time.time() #for science!
    log_it.logg("Starting scraping round", q, genus=["debug"])
    scrapeForums()
    elapsedTime = time.time()-startTime #for science!
    log_it.logg("Scraping round completed successfully", q, genus=["debug"])
    log_it.logg ("Time elapsed in latest scrape: " + str(elapsedTime), q, genus=["benchmarking"])
    if elapsedTime < config.retrieveConfig("Period"): #if the period specified in config hasn't elapsed completely
        log_it.logg("Sleeping",q, genus=["debug"]) #debug
        time.sleep(config.retrieveConfig("Period")-elapsedTime) #sleep until the period time has elapsed

def scrapePost(p, q, check):
    ''' (url : str, Queue object, str)
    scrape post if check is right'''
    startTime = time.time()
    post = scraper.pageClass()
    log_it.logg("Scraping " + p, q, genus=["debug", "verbose"])
    post.ret(p)
    if config.retrieveConfig("NecroDetection")==check:
        if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
            log_it.logg(p + " has been bumped from the dead.", q, genus=["output"])
    if config.retrieveConfig("ProfanityDetection")==check:
        if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
            log_it.logg(p + " has been sworn in a lot.", q, genus=["output"])
    if config.retrieveConfig("CapsTitleDetection")==check:
        if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
            log_it.logg(p + " has a lot of caps in the title.", q, genus=["output"])
    elapsedTime = time.time()-startTime #for science!
    log_it.logg("Finished scraping " + p + " in " + str(elapsedTime), q, genus=["verbose", "benchmarking"])

def scrapeSection(section, q):
    '''(url : str, Queue object)
    scrape a forum section by creating a thread for every page that needs to be scraped'''
    startTime = time.time()
    page = scraper.pageClass()
    threads = []
    page.ret(section)
    check = "all"
    log_it.logg("Creating post scraping threads for " + section, q, genus=["debug"])
    if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
        sectionPosts = page.findAllPosts()
        log_it.logg("Found " + str(len(sectionPosts)) + " threads in section " + section, q, genus=["debug", "verbose"])
        for postNum in range(len(sectionPosts)):
            threads.append(Process(target=scrapePost, args=(sectionPosts[postNum], q, check,)))
            threads[postNum].start()
    check = "first"
    if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
        sectionFirstPost = page.findFirstPost()
        threads.append(Process(target=scrapePost, args=(sectionFirstPost, q, check,)))
        threads[len(threads)].start()

    log_it.logg("Finished creating post scraping threads for " + section, q, genus=["debug"])
    for thread in threads: #wait for all created threads to finish
        thread.join()
    elapsedTime = time.time()-startTime #for science!
    log_it.logg("Time elapsed in scraping section " + section + " : " + str(elapsedTime), q, genus=["verbose", "benchmarking"])

def scrapeForums():
    '''() -> None
    starts the forum section threads'''
    threads=[]
    log_it.logg("Creating section scraping threads", q, genus=["debug"])
    log_it.logg("There are " + str(len(ForumsToCheck.forums)) + " forum sections to scrape", q, genus=["debug", "verbose"])
    for n in range(len(ForumsToCheck.forums)):
        threads.append(Process(target=scrapeSection, args=(ForumsToCheck.forums[n],q,)))
        threads[n].start()
    log_it.logg("Finished creating section scraping threads", q, genus=["debug"])
    for thread in threads: #wait for all created threads to finish
        thread.join()
