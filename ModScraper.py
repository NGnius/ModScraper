'''This actually runs everything'''

import sys, os, time
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, scraper, config, log_it
import necroDetector, profanityDetector, capsDetector
from multiprocessing import Process
page = scraper.pageClass()
post = scraper.pageClass()
def init(queue):
    global q
    q = queue
    

def main(): #main function, goes through the all the stuff
    startTime = time.time() #for science!
    scrapeForums()
    elapsedTime = time.time()-startTime #for science!
    log_it.logg ("Time elapsed in latest scrape: " + str(elapsedTime),q, genus=["debug", "benchmarking"])
    if elapsedTime < config.retrieveConfig("Period"): #if the period specified in config hasn't elapsed completely
        log_it.logg("Sleeping",q, genus=["debug"]) #debug
        time.sleep(config.retrieveConfig("Period")-elapsedTime) #sleep until the period time has elapsed

def scrapePost(p, q, check): #scrape post if check is right
    post = scraper.pageClass()
    log_it.logg("Scraping " + p, q)
    post.ret(p)
    if config.retrieveConfig("NecroDetection")==check:
        if necroDetector.isNecro(post, config.retrieveConfig("NecroTimeDelta")):
            log_it.logg(p + " has been bumped from the dead.",q, genus=["output"])
    if config.retrieveConfig("ProfanityDetection")==check:
        if profanityDetector.isProfanity(post, config.retrieveConfig("SwearThreshold")):
            log_it.logg(p + " has been sworn in a lot.",q, genus=["output"])
    if config.retrieveConfig("CapsTitleDetection")==check:
        if capsDetector.isCapsTitle(post, config.retrieveConfig("CapsTitleThreshold")):
            log_it.logg(p + " has a lot of caps in the title.",q, genus=["output"])

def scrapeSection(section, q): #scrape a forum section by creating a thread for every page that needs to be scraped
    page = scraper.pageClass()
    threads = []
    page.ret(section)
    check = "all"
    log_it.logg("Creating post scraping threads", q, genus=["debug"])
    if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
        sectionPosts = page.findAllPosts()
        for postNum in range(len(sectionPosts)):
            threads.append(Process(target=scrapePost, args=(sectionPosts[postNum], q, check,)))
            threads[postNum].start()
    check = "first"
    if config.retrieveConfig("NecroDetection") == check or config.retrieveConfig("ProfanityDetection") == check or config.retrieveConfig("CapsTitleDetection") == check: #don't run if nothing wants it to
        sectionFirstPost = page.findFirstPost()
        threads.append(Process(target=scrapePost, args=(sectionFirstPost, q, check,)))
        threads[len(threads)].start()

    for thread in threads: #wait for all created threads to finish
        thread.join()

def scrapeForums():
    threads=[]
    log_it.logg("Creating section scraping threads", q, genus=["debug"])
    for n in range(len(ForumsToCheck.forums)):
        threads.append(Process(target=scrapeSection, args=(ForumsToCheck.forums[n],q,)))
        threads[n].start()
    for thread in threads: #wait for all created threads to finish
        thread.join()
