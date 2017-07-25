'''This actually runs everything'''

import sys, os
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, wordSearcher, scraper, necroDetector, profanityDetector

def main(): #main function, goes through the all the stuff
    for i in ForumsToCheck.forums: #check each forum sequentially
        print("Scraping", i) #debug
        if necroDetector.detectNecro(i)==True: #if a necro is detected in section i
            print("A thread has been bumped from the dead in ", i)
        if profanityDetector.detectProfanity(i)==True: #if a lot of swears are detected
            print("A thread has been sworn in a lot in ", i)
