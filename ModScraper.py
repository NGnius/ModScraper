'''This actually runs everything'''

import sys, os, time
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, wordSearcher, scraper, necroDetector, profanityDetector, config

def main(): #main function, goes through the all the stuff
    startTime = time.time()
    for i in ForumsToCheck.forums: #check each forum sequentially
        print("Scraping", i) #debug
        if config.retrieveConfig("NecroDetection").lower() == "first":
            if necroDetector.detectNecro(i)==True: #if a necro is detected in section i
                print("A thread has been bumped from the dead in ", i)
        elif config.retrieveConfig("NecroDetection").lower() == "all":
            detectedNecros = necroDetector.detectAllNecros(i)
            if len(detectedNecros) > 0: #if a necro is detected in section i
                print("The thread(s)", detectedNecros, "has/have been bumped from the dead in ", i)
        if config.retrieveConfig("ProfanityDetection").lower() == "first":
            if profanityDetector.detectProfanity(i)==True: #if a lot of swears are detected
                print("A thread has been sworn in a lot in ", i)
        elif config.retrieveConfig("ProfanityDetection").lower() == "all":
            detectProfanity = profanityDetector.detectAllProfanity(i)
            if len(detectProfanity) > True: #if a lot of swears are detected
                print("The thread(s)", detectedProfanity, "has/have been sworn in a lot in ", i)
    elapsedTime = time.time()-startTime
    if elapsedTime < config.retrieveConfig("Period"): #sleep until the period time has elapsed
        print("Sleeping") #debug
        time.sleep(config.retrieveConfig("Period")-elapsedTime)
