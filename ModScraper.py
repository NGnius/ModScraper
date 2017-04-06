'''This is the continuously running version, which goes through every section
with every function. If you don't want this program to run continuously, don't
run it from this file! (Ignore the fact that there isn't a different file that
allows for the whole program to only be run once)'''
import sys, os
sys.path.append(os.getcwd()+'/Resources')
import ForumsToCheck, wordSearcher, scraper, necroDetector, profanityDetector

while True: #this will continuously go until stopped by force
    for i in ForumsToCheck.forums: #check each forum sequentially
        print("Fuck off, this my URL to scrape:", i) #it can't be debug code with a bit of profanity
        if necroDetector.detectNecro(i)==True: #if a necro is detected in section i
            print("A thread has been bumped from the dead in ", i)
        if profanityDetector.detectProfanity(i)==True: #if a lot of swears are detected
            print("A thread has been sworn in a lot in ", i)
    #print ("Let's do it again!")
